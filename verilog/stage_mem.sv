`include "sys_defs.svh"

module stage_mem (
    input EX_MEM_PACKET ex_mem_reg,

    // Interface to data memory (testbench)
    output logic        dmem_read,
    output logic        dmem_write,
    output logic [31:0] dmem_addr,
    output logic [31:0] dmem_wdata,
    output MEM_SIZE     dmem_size,
    input  logic [31:0] dmem_rdata,

    output MEM_WB_PACKET mem_packet
);

    // Only perform memory operations if the instruction is valid
    assign dmem_read  = ex_mem_reg.rd_mem && ex_mem_reg.valid;
    assign dmem_write = ex_mem_reg.wr_mem && ex_mem_reg.valid;
    
    // Address comes from the ALU result
    assign dmem_addr  = ex_mem_reg.alu_result;
    
    // Data to write comes from rs2
    assign dmem_wdata = ex_mem_reg.rs2_value;
    
    // Size of the memory operation (BYTE, HALF, WORD)
    assign dmem_size  = ex_mem_reg.mem_size;

    logic [31:0] formatted_rdata;

    // Format the read data based on size and sign extension
    always_comb begin
        formatted_rdata = dmem_rdata; // default word
        if (ex_mem_reg.rd_mem) begin
            case (ex_mem_reg.mem_size)
                BYTE: begin
                    if (ex_mem_reg.rd_unsigned)
                        formatted_rdata = {24'b0, dmem_rdata[7:0]};
                    else
                        formatted_rdata = {{24{dmem_rdata[7]}}, dmem_rdata[7:0]};
                end
                HALF: begin
                    if (ex_mem_reg.rd_unsigned)
                        formatted_rdata = {16'b0, dmem_rdata[15:0]};
                    else
                        formatted_rdata = {{16{dmem_rdata[15]}}, dmem_rdata[15:0]};
                end
                WORD: begin
                    formatted_rdata = dmem_rdata;
                end
                default: formatted_rdata = dmem_rdata;
            endcase
        end
    end

    // Pass-throughs and result mux
    // If it's a memory read, the result is the loaded data, otherwise it's the ALU result
    assign mem_packet.result       = (ex_mem_reg.rd_mem) ? formatted_rdata : ex_mem_reg.alu_result;
    assign mem_packet.NPC          = ex_mem_reg.NPC;
    assign mem_packet.dest_reg_idx = ex_mem_reg.dest_reg_idx;
    assign mem_packet.take_branch  = ex_mem_reg.take_branch;
    assign mem_packet.halt         = ex_mem_reg.halt;
    assign mem_packet.illegal      = ex_mem_reg.illegal;
    assign mem_packet.valid        = ex_mem_reg.valid;

endmodule
