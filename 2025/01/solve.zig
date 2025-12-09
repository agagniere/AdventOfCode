const std = @import("std");

const Allocator = std.mem.Allocator;
const Reader = std.Io.Reader;

pub fn day01(alloc: Allocator, input: *Reader) struct { u64, u64 } {
    return solve(alloc, input) catch unreachable;
}

fn solve(alloc: Allocator, input: *Reader) !struct { u64, u64 } {
    var timer: std.time.Timer = try .start();
    const moves = try parse(alloc, input);
    defer alloc.free(moves);
    const t0 = timer.lap();
    const one = part1(moves);
    const t1 = timer.lap();
    const two = part2(moves);
    const t2 = timer.read();

    std.log.info("[01] parse: {D}, ~{D}/line", .{ t0, t0 / moves.len });
    std.log.info("[01] part1: {D}, ~{D}/line", .{ t1, t1 / moves.len });
    std.log.info("[01] part2: {D}, ~{D}/line", .{ t2, t2 / moves.len });
    return .{ one, two };
}

fn part1(moves: []const i16) u32 {
    // The dial starts by pointing at 50.
    var dial: i64 = 50;
    var zeros: u32 = 0;

    for (moves) |move| {
        dial += move;
        if (@mod(dial, 100) == 0)
            zeros += 1;
    }
    return zeros;
}

// For some reason not applying mod to dial every iteration
// resulst in a 3-4x perf boost !?
fn part2(moves: []const i16) u32 {
    var dial: i16 = 50;
    var zeros: i16 = 0;

    for (moves) |move| {
        const dist = if (move < 0 and @mod(dial, 100) != 0)
            100 - @mod(dial, 100) - move
        else if (move < 0)
            -move
        else
            @mod(dial, 100) + move;
        zeros += @divTrunc(dist, 100);
        dial += move;
    }
    return @intCast(zeros);
}

fn parse(alloc: Allocator, input: *Reader) ![]i16 {
    var result: std.ArrayList(i16) = try .initCapacity(alloc, 512);
    defer result.deinit(alloc);

    while (try input.takeDelimiter('\n')) |line| {
        const number = try std.fmt.parseInt(i16, line[1..], 10);
        try result.append(alloc, switch (line[0]) {
            'L' => -number,
            'R' => number,
            else => unreachable,
        });
    }
    return result.toOwnedSlice(alloc);
}

// ---------- Tests ----------

const t = std.testing;

test part1 {
    try t.expectEqual(0, part1(&.{ -68, -30 }));
    try t.expectEqual(1, part1(&.{ -68, -30, 48 }));
    try t.expectEqual(1, part1(&.{ -68, -30, 48, -5, 60 }));
    try t.expectEqual(2, part1(&.{ -68, -30, 48, -5, 60, -55 }));
}

test part2 {
    try t.expectEqual(1, part2(&.{ 10, 50, 50 }));
    try t.expectEqual(1, part2(&.{ 10, -100, 10 }));
    try t.expectEqual(2, part2(&.{ 50, 10, -20 }));
    try t.expectEqual(2, part2(&.{ 10, -20, -40, -10, 20 }));
    try t.expectEqual(4, part2(&.{ 50, 100, 200 }));
    try t.expectEqual(4, part2(&.{ -50, -100, -200 }));
}

test day01 {
    const sample =
        \\L68
        \\L30
        \\R48
        \\L5
        \\R60
        \\L55
        \\L1
        \\L99
        \\R14
        \\L82
    ;
    var stream: Reader = .fixed(sample);
    const list = try parse(t.allocator, &stream);
    defer t.allocator.free(list);

    try t.expectEqualSlices(i16, &.{
        -68,
        -30,
        48,
        -5,
        60,
        -55,
        -1,
        -99,
        14,
        -82,
    }, list);

    try t.expectEqual(3, part1(list));
    try t.expectEqual(6, part2(list));
}
