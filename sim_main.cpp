#include "Vcpu.h"
#include "verilated.h"
#include "verilated_vcd_c.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

// ==========================================
// --- PARAMETERS ---
// Define the desired clock period in nanoseconds
const double CLOCK_PERIOD_NS = 10.0; // 10 ns period = 100 MHz
// ==========================================

// The timescale precision from sys_defs.svh is 100ps (0.1 ns)
// This means 1 unit of main_time = 0.1 ns.
// Therefore, there are 10 time steps per 1 ns.
const double TIME_STEPS_PER_NS = 10.0; 

// Calculate how many simulation time steps make up a half period
const int HALF_PERIOD_STEPS = (int)((CLOCK_PERIOD_NS / 2.0) * TIME_STEPS_PER_NS);

// Required by Verilator to track current simulation time
vluint64_t main_time = 0; 
double sc_time_stamp() { return main_time; }

int main(int argc, char **argv) {
    Verilated::commandArgs(argc, argv);
    Vcpu* top = new Vcpu;

    // --- Load Binary Program into C++ Memory ---
    std::vector<uint8_t> memory;
    const char* prog_name = Verilated::commandArgsPlusMatch("prog=");
    if (prog_name && prog_name[0]) {
        // Extract the actual program name (skip "+prog=")
        std::string filename = std::string("programs/") + (prog_name + 6) + ".bin";
        std::ifstream file(filename, std::ios::binary);
        if (!file) {
            std::cerr << "Failed to open " << filename << std::endl;
            return 1;
        }
        // Read entire binary file into memory vector
        memory.assign(std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>());
        std::cout << "Loaded " << memory.size() << " bytes from " << filename << std::endl;
    } else {
        std::cout << "No program specified. Running with empty memory." << std::endl;
    }

#ifdef TRACE
    Verilated::traceEverOn(true);
    VerilatedVcdC* tfp = new VerilatedVcdC;
    top->trace(tfp, 99);
    tfp->open("wave.vcd");
#endif

    // Initialize inputs
    top->clk = 0;
    top->rst_n = 0; // Assert reset initially

    // Run simulation for 50 full clock cycles
    int max_sim_time = 50 * CLOCK_PERIOD_NS * TIME_STEPS_PER_NS;

    while (main_time < max_sim_time && !Verilated::gotFinish()) {
        
        // Release reset after 2 full clock cycles
        if (main_time > 2 * CLOCK_PERIOD_NS * TIME_STEPS_PER_NS) {
            top->rst_n = 1;
        }

        // Toggle the clock every HALF_PERIOD_STEPS
        if ((main_time % HALF_PERIOD_STEPS) == 0) {
            top->clk = !top->clk;
        }

        // 1. Evaluate to update PC (if clock edge occurred)
        top->eval();

        // 2. Fetch instruction from C++ memory based on current_pc
        uint32_t pc = top->current_pc;
        uint32_t instr = 0;
        
        // Ensure we don't read past the end of our loaded binary
        if (pc + 3 < memory.size()) {
            // Read 4 bytes (little-endian) to form the 32-bit instruction
            instr = memory[pc] | (memory[pc+1] << 8) | (memory[pc+2] << 16) | (memory[pc+3] << 24);
        }
        
        // Drive the instruction into the CPU
        top->fetched_instr = instr;

        // 3. Evaluate again to propagate fetched_instr through combinational logic
        top->eval();

#ifdef TRACE
        // Dump the waveform data at the CURRENT simulation time (in 100ps steps)
        tfp->dump(main_time);
#endif

        // Advance simulation time by 1 step (100ps)
        main_time++;
    }

#ifdef TRACE
    tfp->close();
    delete tfp;
#endif

    delete top;
    return 0;
}
