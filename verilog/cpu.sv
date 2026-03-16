`include "sys_defs.svh"
`include "stage_if.sv"
`include "stage_id.sv"
`include "stage_ex.sv"
`include "stage_mem.sv"
`include "stage_wb.sv"

// ============================================================================
// Top-Level CPU Module
// ============================================================================
module cpu(
    input  logic clk,
    input  logic rst,
    
    // Instruction Memory Interface (driven by C++ testbench)
    output logic [31:0] current_pc,
    /* verilator lint_off UNUSEDSIGNAL */
    input  logic [31:0] fetched_instr,
    /* verilator lint_on UNUSEDSIGNAL */

    // Data Memory Interface (driven by C++ testbench)
    output logic        dmem_read,
    output logic        dmem_write,
    output logic [31:0] dmem_addr,
    output logic [31:0] dmem_wdata,
    output MEM_SIZE     dmem_size,
    input  logic [31:0] dmem_rdata
);

    // Internal signals between stages
    /* verilator lint_off UNUSEDSIGNAL */
    IF_ID_PACKET if_packet, if_id_reg;
    ID_EX_PACKET id_packet, id_ex_reg;
    EX_MEM_PACKET ex_packet, ex_mem_reg;
    MEM_WB_PACKET mem_packet, mem_wb_reg;
    COMMIT_PACKET wb_packet;

    logic if_valid, wb_valid;
    /* verilator lint_on UNUSEDSIGNAL */

    // if_valid should be combinational. If it's in an always_ff, it will be delayed by one clock cycle.
    // We want the IF stage to be valid immediately in the same cycle that reset is deasserted.
    assign if_valid = ~rst || wb_valid;

    // ------------------Fetch Stage------------------
    stage_if stage_if_inst (
      .clk        (clk),
      .rst        (rst),
      .if_valid   (if_valid),
      .take_branch(ex_packet.take_branch),
      .branch_target(ex_packet.alu_result),
      .pc_out     (current_pc),    // Send PC out to testbench memory
      .instr_in   (fetched_instr), // Receive instruction from testbench memory
      .if_packet  (if_packet)
    );

    // IF/ID Reg
    always_ff @(posedge clk) begin
      if (rst) begin
        if_id_reg <= '{
          `NOP, // instr
          32'h0, // PC
          32'h0, // NPC
          `FALSE // valid
        };
      end else begin
        if_id_reg <= if_packet;
      end
    end

    // ------------------Decode Stage------------------
    stage_id stage_id_inst (
      .clk        (clk),
      .rst      (rst),
      .if_id_reg  (if_id_reg),
      .wb_regfile_en   (wb_packet.valid),
      .wb_regfile_idx  (wb_packet.reg_idx),
      .wb_regfile_data (wb_packet.data),
      .id_packet  (id_packet)
    );

    // IF/ID Reg
    always_ff @(posedge clk) begin
      if (rst) begin
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

    // ------------------Execute Stage------------------
    stage_ex stage_ex_inst (
      .id_ex_reg(id_ex_reg),

      .ex_packet(ex_packet)
    );

    // ex/mem reg
    always_ff @(posedge clk) begin
      if (rst) begin
        ex_mem_reg <= '{
          32'b0, // alu result
          32'b0, // NPC
          `FALSE, // take_branch
          32'b0, //rs2_value;
          1'b0, // rd_mem;
          1'b0, // wr_mem;
          `ZERO_REG, // dest_reg_idx;
          1'b0, // halt;
          1'b0, // illegal;
          1'b0, // csr_op;
          1'b0, // rd_unsigned; // Whether our load data is signed or unsigned
          BYTE, // mem_size;
          1'b0 // valid;
        };
      end else begin
        ex_mem_reg <= ex_packet;
      end
    end

    // ------------------Memory Stage------------------
    stage_mem stage_mem_inst (
      .ex_mem_reg(ex_mem_reg),
      
      .dmem_read(dmem_read),
      .dmem_write(dmem_write),
      .dmem_addr(dmem_addr),
      .dmem_wdata(dmem_wdata),
      .dmem_size(dmem_size),
      .dmem_rdata(dmem_rdata),
      
      .mem_packet(mem_packet)
    );

    // mem/wb reg
    always_ff @(posedge clk) begin
      if (rst) begin
        mem_wb_reg <= '{
          32'b0, // result
          32'b0, // NPC
          `ZERO_REG, // dest_reg_idx
          `FALSE, // take_branch
          1'b0, // halt
          1'b0, // illegal
          1'b0  // valid
        };
      end else begin
        mem_wb_reg <= mem_packet;
      end
    end

    // ------------------Writeback Stage------------------
    stage_wb stage_wb_inst (
      .mem_wb_reg(mem_wb_reg),

      .wb_packet(wb_packet)
    );

    always_ff @(posedge clk) begin
        if (rst) wb_valid <= `FALSE;
        else begin
          wb_valid <= mem_wb_reg.valid;
        end
    end

endmodule
