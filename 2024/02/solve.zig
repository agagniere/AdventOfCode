const std = @import("std");
const utils = @import("utils.zig");

const NumberList = std.ArrayList(i32);

fn parse(allocator: std.mem.Allocator, line: []const u8) !NumberList {
    var result = try NumberList.initCapacity(allocator, 10);
    var columns = std.mem.tokenizeScalar(u8, line, ' ');

    while (columns.next()) |column| {
        try result.append(try std.fmt.parseInt(i32, column, 10));
    }
    return result;
}

/// Part 1
fn is_safe(report: []const i32) bool {
    const increasing = report[1] > report[0];

    for (report[0..(report.len - 1)], report[1..]) |level, next| {
        const diff = next - level;
        if (diff == 0 or (diff > 0) != increasing or @abs(diff) > 3)
            return false;
    }
    return true;
}

/// Part 2
fn is_safe_or_almost(report: NumberList) !bool {
    if (is_safe(report.items) or is_safe(report.items[1..]) or is_safe(report.items[0..(report.items.len - 1)]))
        return true;
    for (1..report.items.len - 1) |i| {
        var clone = try report.clone();
        defer clone.deinit();

        _ = clone.orderedRemove(i);
        if (is_safe(clone.items))
            return true;
    }
    return false;
}

fn solve(allocator: std.mem.Allocator, input: anytype) ![2]u32 {
    var result: [2]u32 = .{ 0, 0 };
    var lines = utils.lineIterator(input);

    while (lines.next()) |line| {
        const list = try parse(allocator, line);
        defer list.deinit();

        result[0] += if (is_safe(list.items)) 1 else 0;
        result[1] += if (try is_safe_or_almost(list)) 1 else 0;
    }
    return result;
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());

    const solution = try solve(allocator, stdin.reader());
    std.debug.print("Number of safe reports            : {:10}\n", .{solution[0]});
    std.debug.print("Number of safe (or almost) reports: {:10}\n", .{solution[1]});
}

// -------------------- Tests --------------------

test is_safe {
    try std.testing.expect(is_safe(&.{ 7, 6, 4, 2, 1 }));
    try std.testing.expect(!is_safe(&.{ 1, 2, 7, 8, 9 }));
    try std.testing.expect(!is_safe(&.{ 9, 7, 6, 2, 1 }));
    try std.testing.expect(!is_safe(&.{ 1, 3, 2, 4, 5 }));
    try std.testing.expect(!is_safe(&.{ 8, 6, 4, 4, 1 }));
    try std.testing.expect(is_safe(&.{ 1, 3, 6, 7, 9 }));
}

test is_safe_or_almost {
    const reports: []const struct { result: bool, input: []const i32 } = &.{
        .{ .result = true, .input = &.{ 7, 6, 4, 2, 1 } },
        .{ .result = false, .input = &.{ 1, 2, 7, 8, 9 } },
        .{ .result = false, .input = &.{ 9, 7, 6, 2, 1 } },
        .{ .result = true, .input = &.{ 1, 3, 2, 4, 5 } },
        .{ .result = true, .input = &.{ 8, 6, 4, 4, 1 } },
        .{ .result = true, .input = &.{ 1, 3, 6, 7, 9 } },
    };

    for (reports) |report| {
        var input = try NumberList.initCapacity(std.testing.allocator, 5);
        defer input.deinit();
        try input.appendSlice(report.input);

        try std.testing.expectEqual(report.result, is_safe_or_almost(input));
    }
}

test solve {
    const input =
        \\7 6 4 2 1
        \\1 2 7 8 9
        \\9 7 6 2 1
        \\1 3 2 4 5
        \\8 6 4 4 1
        \\1 3 6 7 9
    ;
    var input_stream = std.io.fixedBufferStream(input);

    const result = try solve(std.testing.allocator, input_stream.reader());
    try std.testing.expectEqual(2, result[0]);
    try std.testing.expectEqual(4, result[1]);
}
