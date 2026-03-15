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
    IF_ID_PACKET if_packet, if_id_reg;
    ID_EX_PACKET id_packet, id_ex_reg;
    /* verilator lint_on UNUSEDSIGNAL */

    // Fetch Stage
    stage_if stage_if_inst (
      .clk        (clk),
      .rst_n      (rst_n),
      .pc_out     (current_pc),    // Send PC out to testbench memory
      .instr_in   (fetched_instr), // Receive instruction from testbench memory
      .if_packet  (if_packet)
    );

    // IF/ID Reg
    always_ff @(posedge clk) begin
      if (!rst_n) begin
        if_id_reg <= if_packet;
      end else begin
        if_id_reg <= '{
          `NOP, // instr
          32'h0, // PC
          32'h0, // NPC
          `FALSE // valid
        };
      end
    end

    // Decode Stage
    stage_id stage_id_inst (
      .clk        (clk),
      .rst_n      (rst_n),
      .if_id_reg  (if_id_reg),
      .wb_regfile_en   (`TRUE),
      .wb_regfile_idx  (`ZERO_REG),
      .wb_regfile_data (32'b0),
      .id_packet  (id_packet)
    );

    // IF/ID Reg
    always_ff @(posedge clk) begin
      if (rst_n) begin
        id_ex_reg <= '{
          `NOP, // we can't simply assign 0 because NOP is non-zero
          32'b0, // PC
          32'b0, // NPC
          32'b0, // rs1 select
          32'b0, // rs2 select
          OPA_IS_RS1,
          OPB_IS_RS2,
          `ZERO_REG,
          ALU_ADD,
          1'b0, // mult
          1'b0, // rd_mem
          1'b0, // wr_mem
          1'b0, // cond
          1'b0, // uncond
          1'b0, // halt
          1'b0, // illegal
          1'b0, // csr_op
          1'b0  // valid
      };
      end else begin
        id_ex_reg <= id_packet;
      end
    end


endmodule
