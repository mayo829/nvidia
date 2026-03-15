`include "sys_defs.svh"
`include "isa.svh"
`include "instr_decoder.sv"

// ============================================================================
// Instruction Decode (ID) Stage
// ============================================================================

module stage_id (
  input logic clk,
  input logic rst_n,
  input IF_ID_PACKET if_id_reg,
  input              wb_regfile_en,   // Reg write enable from WB Stage
  input REG_IDX      wb_regfile_idx,  // Reg write index from WB Stage
  input DATA         wb_regfile_data, // Reg write data from WB Stage

  output ID_EX_PACKET id_packet
);

  assign id_packet.PC = if_id_reg.PC;
  assign id_packet.NPC = if_id_reg.NPC;
  assign id_packet.inst = if_id_reg.inst;
  assign id_packet.valid = if_id_reg.valid;

  logic has_dest;
  assign id_packet.dest_reg_idx = (has_dest) ? if_id_reg.inst.r.rd : `ZERO_REG;

  // Instantiate the register file
  regfile regfile_0 (
    .clock  (clk),
    .read_idx_1 (if_id_reg.inst.r.rs1),
    .read_idx_2 (if_id_reg.inst.r.rs2),
    .write_en   (wb_regfile_en),
    .write_idx  (wb_regfile_idx),
    .write_data (wb_regfile_data),

    .read_out_1 (id_packet.rs1_value),
    .read_out_2 (id_packet.rs2_value)
  );

  instr_decoder decoder_inst (
    .inst(if_id_reg.inst),
    .valid(if_id_reg.valid), // when low, ignore inst. Output will look like a NOP

    .opa_select(id_packet.opa_select),
    .opb_select(id_packet.opb_select),
    .has_dest(has_dest), // if there is a destination register
    .alu_func(id_packet.alu_func),
    .mult(id_packet.mult), 
    .rd_mem(id_packet.rd_mem), 
    .wr_mem(id_packet.wr_mem), 
    .cond_branch(id_packet.cond_branch), 
    .uncond_branch(id_packet.uncond_branch),
    .csr_op(id_packet.csr_op), // used for CSR operations, we only use this as a cheap way to get the return code out
    .halt(id_packet.halt),   // non-zero on a halt
    .illegal(id_packet.illegal) // non-zero on an illegal instruction
  );

endmodule
