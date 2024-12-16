const std = @import("std");
const coro = @import("coroutines");
const Instruction = @import("instruction.zig").Instruction;

const Allocator = std.mem.Allocator;
const NumberList = std.ArrayListUnmanaged(i64);

const InterpreterErrors = error{ CantClone, OutOfInput, CantOutput };

/// Execute the given intcode program.
/// Input is knwon in advance
pub fn interpret(allocator: Allocator, program: []const i64, input: anytype, output: anytype) InterpreterErrors!?i64 {
    var memory: NumberList = .{};
    defer memory.deinit(allocator);
    memory.appendSlice(allocator, program) catch return InterpreterErrors.CantClone;
    var ins = Instruction.init(memory.items);
    var last_output: ?i64 = null;

    while (true) {
        switch (ins.get_type()) {
            .add => {
                ins.argPtr(3).* = ins.arg(1) + ins.arg(2);
                ins.move(4);
            },
            .multiply => {
                ins.argPtr(3).* = ins.arg(1) * ins.arg(2);
                ins.move(4);
            },
            .input => {
                ins.argPtr(1).* = input.recv() orelse return InterpreterErrors.OutOfInput;
                ins.move(2);
            },
            .output => {
                output.send(ins.arg(1)) catch return InterpreterErrors.CantOutput;
                last_output = ins.arg(1);
                ins.move(2);
            },
            .jumpIfTrue => {
                if (ins.arg(1) != 0) {
                    ins.jump(ins.arg(2));
                } else ins.move(3);
            },
            .jumpIfFalse => {
                if (ins.arg(1) == 0) {
                    ins.jump(ins.arg(2));
                } else ins.move(3);
            },
            .lessThan => {
                ins.argPtr(3).* = if (ins.arg(1) < ins.arg(2)) 1 else 0;
                ins.move(4);
            },
            .equals => {
                ins.argPtr(3).* = if (ins.arg(1) == ins.arg(2)) 1 else 0;
                ins.move(4);
            },
            .stop => {
                return last_output;
            },
        }
    }
}
