`include "sys_defs.svh"
`include "stage_if.sv"
`include "stage_id.sv"

// ============================================================================
// Top-Level CPU Module
// ============================================================================
module cpu(
    input  logic clk,
    input  logic rst_n,
    
    // Memory Interface (driven by C++ testbench)
    output logic [31:0] current_pc,
    /* verilator lint_off UNUSEDSIGNAL */
    input  logic [31:0] fetched_instr
    /* verilator lint_on UNUSEDSIGNAL */
);

    // Internal signals between stages
    /* verilator lint_off UNUSEDSIGNAL */
    logic [31:0] if_pc;
    logic [31:0] if_instr;
    logic [31:0] id_pc;
    logic [21:0] id_instr;
    /* verilator lint_on UNUSEDSIGNAL */

    // Fetch Stage
    stage_if stage_if_inst (
        .clk        (clk),
        .rst_n      (rst_n),
        .pc_out     (current_pc),    // Send PC out to testbench memory
        .instr_in   (fetched_instr), // Receive instruction from testbench memory
        .if_pc      (if_pc),         // PC passed down the pipeline
        .if_instr   (if_instr)       // Instruction passed down the pipeline
    );

    // Decode Stage
    stage_id stage_id_inst (
      .clk        (clk),
      .rst_n      (rst_n),
      .if_pc      (if_pc),
      .if_instr   (if_instr),
      .id_pc      (id_pc),
      .id_instr   (id_instr)
    );


endmodule
