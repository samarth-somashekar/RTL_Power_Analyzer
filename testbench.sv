// Code your testbench here
// or browse Examples
`timescale 1ns / 1ps

module tb_counter;
    logic clk;
    logic rst;
    logic [3:0] count;

    counter uut (
        .clk(clk),
        .rst(rst),
        .count(count)
    );

    // Clock generation
    initial clk = 0;
    always #5 clk = ~clk;  // 100 MHz clock

    initial begin
        $dumpfile("counter.vcd");       // Enable VCD output
        $dumpvars(0, tb_counter);       // Dump all variables

        rst = 1;
        #10;
        rst = 0;

        #100;
        $finish;
    end
endmodule
