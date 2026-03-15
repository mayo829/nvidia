build:
	@echo "===== Building Verilator Simulation ====="
	verilator --cc --exe --build -j $(nproc) -Wall sim_main.cpp verilog/cpu.sv
	@echo "===== Build Complete ====="

run: build
	@echo "\n\n===== Running Simulation ====="
	obj_dir/Vcpu
	@echo "===== Simulation Complete ====="

clean:
	@echo "Cleaning build files..."
	rm -rf obj_dir