const std = @import("std");
const utils = @import("utils");

const Point = struct {
    x: i64,
    y: i64,

    pub fn add(self: Point, other: Point) Point {
        return .{ .x = self.x + other.x, .y = self.y + other.y };
    }

    pub fn sub(self: Point, other: Point) Point {
        return .{ .x = self.x - other.x, .y = self.y - other.y };
    }

    pub fn determinant(self: Point, other: Point) i64 {
        return self.x * other.y - self.y * other.x;
    }
};

/// Find integers n and k such that nA + kB = P, and returns 3n + k
pub fn solve(a: Point, b: Point, p: Point) !i64 {
    const det = a.determinant(b);
    if (det == 0) return error.NotLinearIndependant;
    const N = p.determinant(b);
    const K = a.determinant(p);
    return 3 * try std.math.divExact(i64, N, det) + try std.math.divExact(i64, K, det);
}

fn parsePoint(comptime symbol: u8, line: []const u8) !Point {
    const start = std.mem.indexOfScalar(u8, line, symbol).?;
    const end = std.mem.indexOfScalar(u8, line, ',').?;
    const last = std.mem.lastIndexOfScalar(u8, line, symbol).?;

    return .{ .x = try std.fmt.parseUnsigned(i64, line[start + 1 .. end], 10), .y = try std.fmt.parseUnsigned(i64, line[last + 1 ..], 10) };
}

pub fn parse(lines: anytype) ?[3]Point {
    const a = parsePoint('+', lines.next() orelse return null) catch return null;
    const b = parsePoint('+', lines.next() orelse return null) catch return null;
    const p = parsePoint('=', lines.next() orelse return null) catch return null;
    _ = lines.next();

    return .{ a, b, p };
}

pub fn main() !void {
    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());
    var lines = utils.lineIterator(stdin.reader());
    var one: i64 = 0;
    var two: i64 = 0;
    const correction: Point = .{ .x = 10000000000000, .y = 10000000000000 };
    var times: [3]u64 = .{ 0, 0, 0 };
    var timer = try std.time.Timer.start();

    while (parse(&lines)) |tuple| {
        const a, const b, const p = tuple;
        times[0] += timer.lap();
        one += solve(a, b, p) catch 0;
        times[1] += timer.lap();
        two += solve(a, b, p.add(correction)) catch 0;
        times[2] += timer.lap();
    }

    std.debug.print("Tokens to win          : {:16}\n", .{one});
    std.debug.print("Tokens to actually win : {:16}\n", .{two});
    std.debug.print("parse: {}, part1: {}, part2: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]), std.fmt.fmtDuration(times[2]) });
}
