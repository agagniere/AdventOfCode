const std = @import("std");
const utils = @import("utils");

const Allocator = std.mem.Allocator;
const NumberList = std.ArrayListUnmanaged(u64);
const Equation = std.meta.Tuple(&.{ u64, NumberList });

pub fn parse(buffer: *[16]u64, line: []const u8) !Equation {
    const separator = std.mem.indexOfScalar(u8, line, ':').?;
    const result = try std.fmt.parseUnsigned(u64, line[0..separator], 10);
    var numbers = std.mem.tokenizeScalar(u8, line[separator + 1 ..], ' ');
    var list = NumberList.initBuffer(buffer);

    while (numbers.next()) |number| {
        const value = try std.fmt.parseUnsigned(u64, number, 10);
        list.appendAssumeCapacity(value);
    }
    return .{ result, list };
}

fn part1(expected: u64, numbers: []const u64) bool {
    if (numbers.len == 2) {
        return numbers[0] + numbers[1] == expected or numbers[0] * numbers[1] == expected;
    }
    const last = numbers[numbers.len - 1];
    const tail = numbers[0 .. numbers.len - 1];
    if (expected % last == 0 and part1(@divExact(expected, last), tail))
        return true;
    if (expected > last and part1(expected - last, tail))
        return true;
    return false;
}

fn part2(expected: u64, numbers: []const u64) bool {
    if (numbers.len == 2) {
        if (numbers[0] + numbers[1] == expected or numbers[0] * numbers[1] == expected)
            return true;
        var power_of_ten: u64 = 10;
        while (numbers[1] >= power_of_ten)
            power_of_ten *= 10;
        return numbers[0] * power_of_ten + numbers[1] == expected;
    }
    const last = numbers[numbers.len - 1];
    const tail = numbers[0 .. numbers.len - 1];
    if (expected % last == 0 and part2(@divExact(expected, last), tail))
        return true;
    if (expected > last and part2(expected - last, tail))
        return true;
    var power_of_ten: u64 = 10;
    while (last >= power_of_ten)
        power_of_ten *= 10;
    if (expected % power_of_ten == last and part2(@divTrunc(expected, power_of_ten), tail))
        return true;
    return false;
}

pub fn main() !void {
    var buffer: [16]u64 = undefined;
    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());
    var lines = utils.lineIterator(stdin.reader());

    var one: u64 = 0;
    var two: u64 = 0;
    var times: [3]u64 = .{ 0, 0, 0 };
    var timer = try std.time.Timer.start();

    while (lines.next()) |line| {
        const expected, const numbers = try parse(&buffer, line);
        times[0] += timer.lap();
        if (part1(expected, numbers.items))
            one += expected;
        times[1] += timer.lap();
        if (part2(expected, numbers.items))
            two += expected;
        times[2] += timer.lap();
    }
    std.debug.print("Total calibration result with + and *     : {:20}\n", .{one});
    std.debug.print("Total calibration result with +, * and || : {:20}\n", .{two});
    std.debug.print("Parsing: {}, part1: {}, part2: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]), std.fmt.fmtDuration(times[2]) });
}

// -------------------- Tests --------------------

test part1 {
    try std.testing.expectEqual(true, part1(190, &.{ 10, 19 }));
    try std.testing.expectEqual(true, part1(3267, &.{ 81, 40, 27 }));
    try std.testing.expectEqual(true, part1(292, &.{ 11, 6, 16, 20 }));

    try std.testing.expectEqual(false, part1(83, &.{ 17, 5 }));
    try std.testing.expectEqual(false, part1(156, &.{ 15, 6 }));
    try std.testing.expectEqual(false, part1(7290, &.{ 6, 8, 6, 15 }));
    try std.testing.expectEqual(false, part1(161011, &.{ 16, 10, 13 }));
    try std.testing.expectEqual(false, part1(192, &.{ 17, 8, 14 }));
    try std.testing.expectEqual(false, part1(21037, &.{ 9, 7, 18, 13 }));
}

test part2 {
    try std.testing.expectEqual(true, part2(190, &.{ 10, 19 }));
    try std.testing.expectEqual(true, part2(3267, &.{ 81, 40, 27 }));
    try std.testing.expectEqual(true, part2(292, &.{ 11, 6, 16, 20 }));

    try std.testing.expectEqual(true, part2(156, &.{ 15, 6 }));
    try std.testing.expectEqual(true, part2(7290, &.{ 6, 8, 6, 15 }));
    try std.testing.expectEqual(true, part2(192, &.{ 17, 8, 14 }));

    try std.testing.expectEqual(false, part2(83, &.{ 17, 5 }));
    try std.testing.expectEqual(false, part2(161011, &.{ 16, 10, 13 }));
    try std.testing.expectEqual(false, part2(21037, &.{ 9, 7, 18, 13 }));
}
