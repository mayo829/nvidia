# RISC-V CPU Simulation Environment

This repository contains a custom RISC-V CPU written in SystemVerilog, simulated using a high-performance C++ testbench via Verilator.

## How It Works

The simulation bridges the gap between software (C code) and hardware (SystemVerilog) through a fully automated toolchain.

### 1. Software Compilation (`make sim <program>`)
When you run a program (e.g., `make sim count`), the Makefile uses the RISC-V cross-compiler toolchain to translate your C code into raw hardware instructions:
*   `count.c` is compiled into a RISC-V ELF file (`count.elf`) using `riscv64-unknown-elf-gcc` with `-O0` (zero optimization) to preserve all logic for hardware testing.
*   `objcopy` extracts the raw binary machine code into `count.bin`.
*   `objdump` generates a human-readable assembly file (`count.dump`) showing the PC, Hex, and Assembly instructions (using raw `x0-x31` register names) for easy hardware debugging.

### 2. The C++ Testbench (`sim_main.cpp`)
Verilator compiles the SystemVerilog CPU into a C++ class (`Vcpu`). The `sim_main.cpp` file acts as the "motherboard" for this CPU:
*   **Memory:** It reads the `count.bin` file into a C++ `std::vector<uint8_t>`, which acts as the system's instruction memory.
*   **Clock:** It contains a `while` loop that toggles the `clk` signal based on a parameterized timescale (currently set to 100MHz / 10ns period).
*   **Synchronous Execution (`top->eval()`):** The testbench and CPU run in lockstep. When the C++ code calls `top->eval()`, the testbench pauses, and the Verilog logic evaluates its current inputs (updating flip-flops on clock edges and propagating combinational logic). The C++ testbench only resumes once the hardware has fully settled, ensuring it never "misses" a PC update.
*   **Instruction Fetching:** Every cycle, the C++ testbench reads the `current_pc` output from the Verilog CPU, looks up the corresponding 4 bytes in the C++ memory vector, and drives that 32-bit instruction into the CPU's `fetched_instr` input pin before calling `eval()` again.

### 3. The Hardware (`verilog/cpu.sv`)
The CPU is designed as a standard pipeline:
*   **Fetch Stage (`stage_if.sv`):** Contains the Program Counter (`pc_reg`). On every clock cycle, it increments the PC by 4 and outputs it to the testbench to request the next instruction.
*   The fetched instruction is then passed down the pipeline for decoding and execution.

## Usage

To run a C program and view the waveform:
```bash
make sim count
```
This will compile `programs/count.c`, run the Verilator simulation, and automatically open GTKWave to view the `wave.vcd` output.

To view the assembly instructions for debugging:
```bash
cat programs/count.dump
```