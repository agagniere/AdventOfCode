const std = @import("std");
const Instruction = @import("instruction.zig").Instruction;

const Allocator = std.mem.Allocator;
const NumberList = std.ArrayListUnmanaged(i64);

const Result = struct {
    first_byte: i64,
    output: []i64,
};

/// Execute the given intcode program.
/// Input is knwon in advance
pub fn interpret(allocator: Allocator, program: []const i64, _input: []const i64) !Result {
    var output: NumberList = .{};
    var input: NumberList = .{};
    defer input.deinit(allocator);
    var memory: NumberList = .{};
    defer memory.deinit(allocator);

    try input.appendSlice(allocator, _input);
    std.mem.reverse(i64, input.items);
    try memory.appendSlice(allocator, program);
    var ins = Instruction.init(memory.items);

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
                ins.argPtr(1).* = input.popOrNull() orelse return error.OutOfInput;
                //std.log.debug("Read: {}", .{ins.arg(1)});
                ins.move(2);
            },
            .output => {
                try output.append(allocator, ins.arg(1));
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
                return .{ .first_byte = memory.items[0], .output = try output.toOwnedSlice(allocator) };
            },
        }
    }
}

test "day2" {
    try std.testing.expectEqual(3500, (try interpret(std.testing.allocator, &.{ 1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50 }, &.{})).first_byte);
}

test "day5" {
    const program = .{ 3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99 };
    const below = try interpret(std.testing.allocator, &program, &.{-8});
    defer std.testing.allocator.free(below.output);
    const above = try interpret(std.testing.allocator, &program, &.{99});
    defer std.testing.allocator.free(above.output);
    const eight = try interpret(std.testing.allocator, &program, &.{8});
    defer std.testing.allocator.free(eight.output);

    try std.testing.expectEqual(999, below.output[0]);
    try std.testing.expectEqual(1000, eight.output[0]);
    try std.testing.expectEqual(1001, above.output[0]);
}
