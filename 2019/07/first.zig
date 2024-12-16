const std = @import("std");
const parse = @import("parse.zig").parse;
const interpret = @import("sequential.zig").interpret;

const Allocator = std.mem.Allocator;
const NumberList = std.ArrayListUnmanaged(i64);

fn chain(allocator: Allocator, program: []const i64, phase_settings: [5]usize) !i64 {
    var signal: i64 = 0;

    for (phase_settings) |phase| {
        const result = try interpret(allocator, program, &.{ @as(i64, @intCast(phase)), signal });
        defer allocator.free(result.output);
        signal = result.output[0];
    }
    return signal;
}

fn solve(allocator: Allocator, program: []const i64) !i64 {
    var max: i64 = 0;

    for (0..5) |a| {
        for (0..5) |b| {
            if (b == a)
                continue;
            for (0..5) |c| {
                if (c == a or c == b)
                    continue;
                for (0..5) |d| {
                    if (d == a or d == b or d == c)
                        continue;
                    for (0..5) |e| {
                        if (e == a or e == b or e == c or e == d)
                            continue;
                        max = @max(max, try chain(allocator, program, .{ a, b, c, d, e }));
                    }
                }
            }
        }
    }
    return max;
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());
    var times: [2]u64 = .{ 0, 0 };
    var timer = try std.time.Timer.start();

    const program = try parse(allocator, stdin.reader());
    defer allocator.free(program);
    times[0] += timer.lap();
    const one = try solve(allocator, program);
    times[1] += timer.lap();

    std.debug.print("Max signal: {}\n", .{one});
    std.debug.print("parse: {}, part1: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]) });
}

test "part1" {
    const one = .{ 3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0 };
    const two = .{ 3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0 };
    const three = .{ 3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0 };

    try std.testing.expectEqual(43210, try solve(std.testing.allocator, &one));
    try std.testing.expectEqual(54321, try solve(std.testing.allocator, &two));
    try std.testing.expectEqual(65210, try solve(std.testing.allocator, &three));
}
