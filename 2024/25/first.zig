const std = @import("std");
const utils = @import("utils");

const Allocator = std.mem.Allocator;
const NumberList = std.ArrayListUnmanaged(u64);

pub fn parse(allocator: Allocator, input: anytype) !NumberList {
    var result: NumberList = .empty;
    var lines = utils.lineIterator(input);

    while (lines.next()) |line| {
        const value = try std.fmt.parseUnsigned(u64, line, 16);
        try result.append(allocator, value);
    }
    return result;
}

pub fn solve(locksAndKeys: []u64) !u32 {
    var result: u32 = 0;

    for (locksAndKeys, 0..) |a, i| {
        for (locksAndKeys[i + 1 ..]) |b| {
            if (a & b == 0)
                result += 1;
        }
    }
    return result;
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());
    var timer = try std.time.Timer.start();
    var times: [2]u64 = .{ 0, 0 };

    var input = try parse(allocator, stdin.reader());
    defer input.deinit(allocator);
    times[0] = timer.lap();
    const matches = try solve(input.items);
    times[1] = timer.read();

    std.debug.print("{}\n", .{matches});
    std.debug.print("parse: {}, solve: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]) });
}
