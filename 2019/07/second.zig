const std = @import("std");
const coro = @import("coroutines");
const parse = @import("parse.zig").parse;
const interpret = @import("async.zig").interpret;

const Allocator = std.mem.Allocator;
const Channel = coro.Channel(i64, .{ .capacity = 3 });

fn chain(allocator: Allocator, program: []const i64, phase_settings: [5]i64) !i64 {
    std.log.debug("Chain: program is {} bytes long", .{program.len});

    var exec = coro.Executor.init();
    coro.initEnv(.{ .stack_allocator = allocator, .executor = &exec });

    std.log.debug("Initialized environment", .{});

    var ea = Channel.init(null);
    var ab = Channel.init(null);
    var bc = Channel.init(null);
    var cd = Channel.init(null);
    var de = Channel.init(null);

    std.log.debug("Created channels", .{});

    try ea.send(phase_settings[0]);
    try ea.send(0);
    try ab.send(phase_settings[1]);
    try bc.send(phase_settings[2]);
    try cd.send(phase_settings[3]);
    try de.send(phase_settings[4]);

    std.log.debug("Wrote to channels", .{});

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

    std.log.debug("Created co-routines", .{});

    while (exec.tick()) {}

    std.log.debug("Done looping", .{});
    const signal: ?i64 = try coro.xawait(E);
    return signal.?;
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

    const two = try chain(allocator, program, .{ 9, 8, 7, 6, 5 });

    std.debug.print("Singal: {}\n", .{two});
    std.debug.print("parse: {}, part1: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]) });
}

test "part2" {}
