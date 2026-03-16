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
    // We allocate 16 MB of memory to simulate a real RAM space.
    // This allows the stack pointer (which often starts at 0 and decrements)
    // to wrap around and safely access the top of memory.
    std::vector<uint8_t> memory(16 * 1024 * 1024, 0); // 16 MB
    uint32_t mem_mask = memory.size() - 1;

    const char* prog_name = Verilated::commandArgsPlusMatch("prog=");
    if (prog_name && prog_name[0]) {
        // Extract the actual program name (skip "+prog=")
        std::string filename = std::string("programs/") + (prog_name + 6) + ".bin";
        std::ifstream file(filename, std::ios::binary | std::ios::ate);
        if (file) {
            std::streamsize size = file.tellg();
            file.seekg(0, std::ios::beg);
            if (size > memory.size()) size = memory.size();
            file.read(reinterpret_cast<char*>(memory.data()), size);
            std::cout << "Loaded " << size << " bytes from " << filename << std::endl;
        } else {
            std::cerr << "Failed to open " << filename << std::endl;
            return 1;
        }
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
    top->rst = 1; // Assert reset initially

    // Run simulation for 50 full clock cycles
    int max_sim_time = 50 * CLOCK_PERIOD_NS * TIME_STEPS_PER_NS;

    while (main_time < max_sim_time && !Verilated::gotFinish()) {
        
        // Release reset after 2 full clock cycles
        if (main_time > 2 * CLOCK_PERIOD_NS * TIME_STEPS_PER_NS) {
            top->rst = 0;
        }

        bool clk_prev = top->clk;

        // Toggle the clock every HALF_PERIOD_STEPS
        if ((main_time % HALF_PERIOD_STEPS) == 0) {
            top->clk = !top->clk;
        }

        bool falling_edge = (clk_prev && !top->clk);

        // 1. Evaluate to update PC (if clock edge occurred)
        top->eval();

        // 2. Fetch instruction from C++ memory based on current_pc
        uint32_t pc = top->current_pc & mem_mask;
        uint32_t instr = memory[pc] | (memory[pc+1] << 8) | (memory[pc+2] << 16) | (memory[pc+3] << 24);
        
        // Drive the instruction into the CPU
        top->fetched_instr = instr;

        // 3. Data Memory Read (Combinational)
        uint32_t dmem_addr = top->dmem_addr & mem_mask;
        uint32_t rdata = 0;
        if (top->dmem_read) {
            if (top->dmem_size == 0) { // BYTE
                rdata = memory[dmem_addr];
            } else if (top->dmem_size == 1) { // HALF
                rdata = memory[dmem_addr] | (memory[dmem_addr+1] << 8);
            } else { // WORD
                rdata = memory[dmem_addr] | (memory[dmem_addr+1] << 8) | 
                        (memory[dmem_addr+2] << 16) | (memory[dmem_addr+3] << 24);
            }
        }
        top->dmem_rdata = rdata;

        // 4. Evaluate again to propagate fetched_instr and dmem_rdata through combinational logic
        top->eval();

        // 5. Data Memory Write (Synchronous, done safely on the falling edge)
        if (falling_edge && top->dmem_write) {
            uint32_t addr = top->dmem_addr & mem_mask;
            uint32_t wdata = top->dmem_wdata;
            if (top->dmem_size == 0) { // BYTE
                memory[addr] = wdata & 0xFF;
            } else if (top->dmem_size == 1) { // HALF
                memory[addr] = wdata & 0xFF;
                memory[addr+1] = (wdata >> 8) & 0xFF;
            } else { // WORD
                memory[addr] = wdata & 0xFF;
                memory[addr+1] = (wdata >> 8) & 0xFF;
                memory[addr+2] = (wdata >> 16) & 0xFF;
                memory[addr+3] = (wdata >> 24) & 0xFF;
            }
        }

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
