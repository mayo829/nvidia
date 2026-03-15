.PHONY: run sim clean

# Extract the first argument as the target (e.g., "run" or "sim")
# and use the rest as arguments for that target.
ifeq (run,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets so make won't complain
  $(eval $(RUN_ARGS):;@:)
endif

ifeq (sim,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "sim"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets so make won't complain
  $(eval $(RUN_ARGS):;@:)
endif

# If no program is provided, default to 'default_prog'
PROG = $(if $(RUN_ARGS),$(RUN_ARGS),default_prog)

# --- RISC-V Toolchain ---
CC = riscv64-unknown-elf-gcc
OBJCOPY = riscv64-unknown-elf-objcopy
OBJDUMP = riscv64-unknown-elf-objdump

# Compile C to ELF (using basic RV32I architecture)
programs/%.elf: programs/%.c
	$(CC) -march=rv32i -mabi=ilp32 -O0 -nostdlib -nostartfiles -Ttext 0x0 -o $@ $<

# Convert ELF to Binary (raw machine code)
programs/%.bin: programs/%.elf
	$(OBJCOPY) -O binary $< $@

# Generate Assembly Dump for debugging
programs/%.dump: programs/%.elf
	$(OBJDUMP) -d -M numeric,no-aliases $< > $@

# Normal build
obj_dir/Vcpu:
	verilator --cc --exe --build -j $(nproc) -Wall -Iverilog sim_main.cpp verilog/cpu.sv

# Build + VCD tracing
obj_dir/Vcpu_trace:
	verilator --cc --exe --build -j $(nproc) -Wall --trace -Iverilog -CFLAGS "-DTRACE" sim_main.cpp verilog/cpu.sv -o Vcpu_trace

# Run normal simulation
run: programs/$(PROG).bin programs/$(PROG).dump obj_dir/Vcpu
	./obj_dir/Vcpu +prog=$(PROG)

# Run simulation with VCD
sim: clean programs/$(PROG).bin programs/$(PROG).dump obj_dir/Vcpu_trace
	./obj_dir/Vcpu_trace +prog=$(PROG)
	gtkwave wave.vcd &

clean:
	rm -rf obj_dir
	rm -rf wave.vcd
	rm -rf programs/*.elf
	rm -rf programs/*.bin
	rm -rf programs/*.hex
	rm -rf programs/*.dump