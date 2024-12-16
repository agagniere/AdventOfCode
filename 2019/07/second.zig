const std = @import("std");
const coro = @import("coroutines");
const parse = @import("parse.zig").parse;
const interpret = @import("async.zig").interpret;

const Allocator = std.mem.Allocator;
const Channel = coro.Channel(i64, .{ .capacity = 3 });

fn chain(allocator: Allocator, program: []const i64, phase_settings: [5]i64) !i64 {
    var exec = coro.Executor.init();
    coro.initEnv(.{ .stack_allocator = allocator, .executor = &exec });

    var ea = Channel.init(null);
    var ab = Channel.init(null);
    var bc = Channel.init(null);
    var cd = Channel.init(null);
    var de = Channel.init(null);

    try ea.send(phase_settings[0]);
    try ea.send(0);
    try ab.send(phase_settings[1]);
    try bc.send(phase_settings[2]);
    try cd.send(phase_settings[3]);
    try de.send(phase_settings[4]);

    const A = try coro.xasync(interpret, .{ allocator, program, &ea, &ab }, null);
    defer A.deinit();
    const B = try coro.xasync(interpret, .{ allocator, program, &ab, &bc }, null);
    defer B.deinit();
    const C = try coro.xasync(interpret, .{ allocator, program, &bc, &cd }, null);
    defer C.deinit();
    const D = try coro.xasync(interpret, .{ allocator, program, &cd, &de }, null);
    defer D.deinit();
    const E = try coro.xasync(interpret, .{ allocator, program, &de, &ea }, null);
    defer E.deinit();

    while (exec.tick()) {}
    return (try coro.xawait(E)).?;
}

fn solve(allocator: Allocator, program: []const i64) !i64 {
    var max: i64 = 0;

    for (5..10) |a| {
        for (5..10) |b| {
            if (b == a)
                continue;
            for (5..10) |c| {
                if (c == a or c == b)
                    continue;
                for (5..10) |d| {
                    if (d == a or d == b or d == c)
                        continue;
                    for (5..10) |e| {
                        if (e == a or e == b or e == c or e == d)
                            continue;
                        max = @max(max, try chain(allocator, program, .{
                            @as(i64, @intCast(a)),
                            @as(i64, @intCast(b)),
                            @as(i64, @intCast(c)),
                            @as(i64, @intCast(d)),
                            @as(i64, @intCast(e)),
                        }));
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

    const two = try solve(allocator, program);
    times[1] += timer.lap();

    std.debug.print("Max signal: {}\n", .{two});
    std.debug.print("parse: {}, part2: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]) });
}

test "part2" {
    const one = .{ 3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5 };
    const two = .{ 3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10 };

    try std.testing.expectEqual(139629729, try solve(std.testing.allocator, &one));
    try std.testing.expectEqual(18216, try solve(std.testing.allocator, &two));
}
