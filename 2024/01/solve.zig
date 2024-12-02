const std = @import("std");
const utils = @import("utils.zig");

const NumberList = std.ArrayList(u32);
const Histogram = std.AutoHashMap(u32, u32);

const Day01 = struct {
    left: NumberList,
    right: NumberList,

    pub fn release(self: @This()) void {
        self.left.deinit();
        self.right.deinit();
    }
};

fn parse(allocator: std.mem.Allocator, input: anytype) !Day01 {
    var left = try NumberList.initCapacity(allocator, 1000);
    var right = try NumberList.initCapacity(allocator, 1000);
    var lines = utils.lineIterator(input);

    while (lines.next()) |line| {
        var columns = std.mem.tokenizeScalar(u8, line, ' ');
        try left.append(try std.fmt.parseInt(u32, columns.next().?, 10));
        try right.append(try std.fmt.parseInt(u32, columns.next().?, 10));
    }

    return .{ .left = left, .right = right };
}

fn part1(input: Day01) u64 {
    var result: u64 = 0;

    std.sort.pdq(u32, input.left.items, {}, std.sort.asc(u32));
    std.sort.pdq(u32, input.right.items, {}, std.sort.asc(u32));

    for (input.left.items, input.right.items) |a, b| {
        result += @max(a, b) - @min(a, b);
    }
    return result;
}

fn part2(allocator: std.mem.Allocator, input: Day01) !u64 {
    var result: u64 = 0;
    var count = Histogram.init(allocator);
    defer count.deinit();

    for (input.right.items) |b| {
        try count.put(b, 1 + (count.get(b) orelse 0));
    }
    for (input.left.items) |a| {
        result += a * (count.get(a) orelse 0);
    }
    return result;
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());

    const input = try parse(allocator, stdin.reader());
    defer input.release();

    std.debug.print("lists total distance  : {:10}\n", .{part1(input)});
    std.debug.print("lists similarity score: {:10}\n", .{try part2(allocator, input)});
}

// -------------------- Tests --------------------

test {
    const sample =
        \\3   4
        \\4   3
        \\2   5
        \\1   3
        \\3   9
        \\3   3
    ;
    var stream = std.io.fixedBufferStream(sample);
    const input = try parse(std.testing.allocator, stream.reader());
    defer input.release();

    try std.testing.expectEqual(11, part1(input));
    try std.testing.expectEqual(31, try part2(std.testing.allocator, input));
}
