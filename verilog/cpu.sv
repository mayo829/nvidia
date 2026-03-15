`include "sys_defs.svh"
`include "stage_if.sv"

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
    /* verilator lint_on UNUSEDSIGNAL */

    // Instantiate the Fetch Stage
    stage_if stage_if_inst (
        .clk        (clk),
        .rst_n      (rst_n),
        .pc_out     (current_pc),    // Send PC out to testbench memory
        .instr_in   (fetched_instr), // Receive instruction from testbench memory
        .if_pc      (if_pc),         // PC passed down the pipeline
        .if_instr   (if_instr)       // Instruction passed down the pipeline
    );

    // Next step: Instantiate Decode Stage here...
    // decode_stage ID_STAGE ( ... );



endmodule
