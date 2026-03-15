`include "sys_defs.svh"

// ============================================================================
// Instruction Fetch (IF) Stage
// ============================================================================
module stage_if (
    input  logic        clk,
    input  logic        rst_n,
    
    // Interface to Instruction Memory (simulated in testbench)
    output logic [31:0] pc_out,
    input  logic [31:0] instr_in,
    
    // Interface to Decode Stage
    output logic [31:0] if_pc,
    output logic [31:0] if_instr
);

    logic [31:0] pc_reg;

    // PC Register
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            pc_reg <= 32'h0;
        end else begin
            pc_reg <= pc_reg + 4; // Advance PC by 4 bytes (1 word)
        end
    end

    // Output current PC to memory to fetch the instruction
    assign pc_out = pc_reg;

    // Pass the PC and fetched instruction down the pipeline
    assign if_pc = pc_reg;
    assign if_instr = instr_in;

endmodule
