const std = @import("std");
const utils = @import("utils");

const Allocator = std.mem.Allocator;
const PointList = std.BoundedArray(Point, 4);
const PointSet = std.AutoHashMapUnmanaged(Point, void);
const PointsPerFrequency = std.AutoArrayHashMapUnmanaged(u8, PointList);

const Point = struct {
    x: i32,
    y: i32,

    pub fn add(self: Point, other: Point) Point {
        return .{ .x = self.x + other.x, .y = self.y + other.y };
    }

    pub fn sub(self: Point, other: Point) Point {
        return .{ .x = self.x - other.x, .y = self.y - other.y };
    }

    pub fn isInBounds(self: Point, bounds: Point) bool {
        return self.x >= 0 and self.y >= 0 and self.x < bounds.x and self.y < bounds.y;
    }
};

pub fn parse(allocator: Allocator, input: anytype) !struct { PointsPerFrequency, Point } {
    var antennas: PointsPerFrequency = .empty;
    var bound_x: i32 = 0;
    var y: i32 = 0;
    var lines = utils.lineIterator(input);

    try antennas.ensureTotalCapacity(allocator, 26 * 2 + 10);
    while (lines.next()) |line| {
        bound_x = @intCast(line.len);
        for (line, 0..line.len) |c, x| {
            if (c != '.') {
                var antenna = try antennas.getOrPutValue(allocator, c, try PointList.init(0));
                antenna.value_ptr.appendAssumeCapacity(.{ .x = @intCast(x), .y = y });
            }
        }
        y += 1;
    }
    return .{ antennas, .{ .x = bound_x, .y = y } };
}

const AntinodeIterator = struct {
    a: Point,
    b: Point,
    delta: Point,

    pub fn init(p1: Point, p2: Point) AntinodeIterator {
        return .{ .a = p1, .b = p2, .delta = p2.sub(p1) };
    }

    pub fn next(self: *AntinodeIterator, bounds: Point) ?Point {
        var result: ?Point = null;
        if (self.a.isInBounds(bounds)) {
            result = self.a;
            self.a = self.a.sub(self.delta);
        } else if (self.b.isInBounds(bounds)) {
            result = self.b;
            self.b = self.b.add(self.delta);
        }
        return result;
    }
};

fn part1(allocator: Allocator, antennas: PointsPerFrequency, bounds: Point) u64 {
    var frequencies = antennas.iterator();
    var antinodes: PointSet = .empty;

    antinodes.ensureTotalCapacity(allocator, @intCast(@divTrunc(bounds.x * bounds.y, 10))) catch unreachable;
    while (frequencies.next()) |frequency| {
        const positions = frequency.value_ptr.slice();
        for (0..positions.len, positions) |i, p1| {
            for (positions[i + 1 ..]) |p2| {
                const nodes = [_]Point{ p1.sub(p2.sub(p1)), p2.add(p2.sub(p1)) };
                for (nodes) |node| {
                    if (node.isInBounds(bounds))
                        antinodes.putAssumeCapacity(node, {});
                }
            }
        }
    }
    return antinodes.count();
}

fn part2(allocator: Allocator, antennas: PointsPerFrequency, bounds: Point) u64 {
    var frequencies = antennas.iterator();
    var antinodes: PointSet = .empty;

    antinodes.ensureTotalCapacity(allocator, @intCast(@divTrunc(bounds.x * bounds.y, 2))) catch unreachable;
    while (frequencies.next()) |frequency| {
        const positions = frequency.value_ptr.slice();
        for (0..positions.len, positions) |i, p1| {
            for (positions[i + 1 ..]) |p2| {
                var nodes = AntinodeIterator.init(p1, p2);
                while (nodes.next(bounds)) |node| {
                    antinodes.putAssumeCapacity(node, {});
                }
            }
        }
    }
    return antinodes.count();
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());
    var timer = try std.time.Timer.start();
    var times: [3]u64 = undefined;

    const antennas, const bounds = try parse(alloc, stdin.reader());
    times[0] = timer.lap();
    const one = part1(alloc, antennas, bounds);
    times[1] = timer.lap();
    const two = part2(alloc, antennas, bounds);
    times[2] = timer.lap();

    std.debug.print("Number of 2:1 antinodes : {:8}\n", .{one});
    std.debug.print("Number of antinodes     : {:8}\n", .{two});
    std.debug.print("parse: {}, part1: {}, part2: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]), std.fmt.fmtDuration(times[2]) });
}

test {
    const sample =
        \\............
        \\........0...
        \\.....0......
        \\.......0....
        \\....0.......
        \\......A.....
        \\............
        \\............
        \\........A...
        \\.........A..
        \\............
        \\............
    ;
    var stream = std.io.fixedBufferStream(sample);
    var arena = std.heap.ArenaAllocator.init(std.testing.allocator);
    defer arena.deinit();
    const alloc = arena.allocator();

    const antennas, const bounds = try parse(alloc, stream.reader());

    try std.testing.expectEqual(14, part1(alloc, antennas, bounds));
    try std.testing.expectEqual(34, part2(alloc, antennas, bounds));
}
