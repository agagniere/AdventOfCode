const std = @import("std");

pub const InstructionType = enum(u8) {
    add = 1,
    multiply,
    input,
    output,
    jumpIfTrue,
    jumpIfFalse,
    lessThan,
    equals,
    stop = 99,
};

pub const Instruction = struct {
    program: [*]i64,
    current: [*]i64,

    pub fn init(_program: []i64) Instruction {
        return .{ .program = _program.ptr, .current = _program.ptr };
    }

    pub inline fn get_type(self: Instruction) InstructionType {
        return @enumFromInt(@mod(self.current[0], 100));
    }

    pub fn argPtr(self: Instruction, comptime index: usize) *i64 {
        const spot = comptime try std.math.powi(i64, 10, index + 1);
        const is_immediate: bool =
            if (@mod(@divTrunc(self.current[0], spot), 2) == 1)
            true
        else
            false;
        if (is_immediate)
            return &self.current[index];
        return &self.program[@intCast(self.current[index])];
    }

    pub inline fn arg(self: Instruction, comptime index: usize) i64 {
        return self.argPtr(index).*;
    }

    pub fn move(self: *Instruction, n: usize) void {
        self.current += n;
    }

    pub fn jump(self: *Instruction, index: i64) void {
        self.current = self.program + @as(usize, @intCast(index));
    }
};
