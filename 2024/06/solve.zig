const std = @import("std");
const utils = @import("utils");

const PointSet = std.AutoHashMap(Point, void);
const InitialSituation = std.meta.Tuple(&.{ Point, Cardinal, PointSet, Point });
const Allocator = std.mem.Allocator;
const OrientedPointSet = std.AutoHashMap(std.meta.Tuple(&.{ Point, Cardinal }), void);

const Cardinal = enum(u2) {
    north,
    west,
    south,
    east,

    pub fn fromChar(c: u8) !Cardinal {
        return switch (c) {
            '^' => .north,
            '>' => .west,
            'v' => .south,
            '<' => .east,
            else => error.InvalidChar,
        };
    }
};

const Point = struct {
    x: i32,
    y: i32,

    pub fn add(self: Point, other: Point) Point {
        return .{ .x = self.x + other.x, .y = self.y + other.y };
    }

    pub fn neighbor(self: Point, direction: Cardinal) Point {
        return switch (direction) {
            .north => self.add(.{ .x = 0, .y = -1 }),
            .west => self.add(.{ .x = 1, .y = 0 }),
            .south => self.add(.{ .x = 0, .y = 1 }),
            .east => self.add(.{ .x = -1, .y = 0 }),
        };
    }

    pub fn isInBounds(self: Point, bounds: Point) bool {
        return self.x >= 0 and self.y >= 0 and self.x < bounds.x and self.y < bounds.y;
    }
};

pub fn parse(allocator: Allocator, input: anytype) !InitialSituation {
    var obstacles = PointSet.init(allocator);
    var guard: ?Point = null;
    var facing: ?Cardinal = null;
    var lines = utils.lineIterator(input);
    var max_x: i32 = 0;
    var y: i32 = 0;

    while (lines.next()) |line| {
        for (line, 0..line.len) |c, x| {
            if (c == '#') {
                try obstacles.put(.{ .x = @intCast(x), .y = y }, {});
            } else if (std.mem.indexOfScalar(u8, "^>v<", c)) |_| {
                guard = .{ .x = @intCast(x), .y = y };
                facing = try Cardinal.fromChar(c);
            }
            if (x > max_x)
                max_x = @intCast(x);
        }
        y += 1;
    }
    return .{ guard.?, facing.?, obstacles, .{ .x = max_x + 1, .y = y } };
}

fn part1(allocator: Allocator, guardPos: Point, guardDir: Cardinal, obstacles: PointSet, bounds: Point) !u64 {
    var visited = PointSet.init(allocator);
    defer visited.deinit();
    var current = guardPos;
    var facing = guardDir;

    while (current.isInBounds(bounds)) {
        try visited.put(current, {});
        const peek = current.neighbor(facing);
        if (obstacles.contains(peek)) {
            facing = @enumFromInt(@intFromEnum(facing) +% 1);
        } else {
            current = peek;
        }
    }

    return visited.count();
}

fn isInLoop(allocator: Allocator, guardPos: Point, guardDir: Cardinal, obstacles: PointSet, bounds: Point) !bool {
    var visited = OrientedPointSet.init(allocator);
    defer visited.deinit();
    var current = guardPos;
    var facing = guardDir;

    while (current.isInBounds(bounds)) {
        if (visited.contains(.{ current, facing }))
            return true;
        try visited.put(.{ current, facing }, {});
        const peek = current.neighbor(facing);
        if (obstacles.contains(peek)) {
            facing = @enumFromInt(@intFromEnum(facing) +% 1);
        } else {
            current = peek;
        }
    }
    return false;
}

fn part2(allocator: Allocator, guardPos: Point, guardDir: Cardinal, obstacles: PointSet, bounds: Point) !u64 {
    var current = guardPos;
    var facing = guardDir;
    var possibleExtras = PointSet.init(allocator);
    defer possibleExtras.deinit();

    while (current.isInBounds(bounds)) {
        const peek = current.neighbor(facing);
        if (obstacles.contains(peek)) {
            facing = @enumFromInt(@intFromEnum(facing) +% 1);
        } else {
            if (peek.isInBounds(bounds) and !possibleExtras.contains(peek)) {
                var obstacles_with_extra = try obstacles.clone();
                defer obstacles_with_extra.deinit();

                try obstacles_with_extra.put(peek, {});
                if (try isInLoop(allocator, current, facing, obstacles_with_extra, bounds))
                    try possibleExtras.put(peek, {});
            }
            current = peek;
        }
    }

    for (0..@intCast(bounds.y)) |y| {
        for (0..@intCast(bounds.x)) |x| {
            const p = Point{ .x = @intCast(x), .y = @intCast(y) };
            if (obstacles.contains(p)) {
                std.debug.print("#", .{});
            } else if (possibleExtras.contains(p)) {
                std.debug.print("O", .{});
            } else {
                std.debug.print(".", .{});
            }
        }
        std.debug.print("\n", .{});
    }

    return possibleExtras.count();
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());

    const guardPos, const guardDir, var obstacles, const bounds = try parse(allocator, stdin.reader());
    defer obstacles.deinit();

    std.debug.print("Number of cells visited : {:5}\n", .{try part1(allocator, guardPos, guardDir, obstacles, bounds)});
    std.debug.print("Number of possible loops: {:5}\n", .{try part2(allocator, guardPos, guardDir, obstacles, bounds)});
}
// < 2007 < 2171
// -------------------- Tests --------------------

test {
    const sample =
        \\....#.....
        \\.........#
        \\..........
        \\..#.......
        \\.......#..
        \\..........
        \\.#..^.....
        \\........#.
        \\#.........
        \\......#...
    ;
    var stream = std.io.fixedBufferStream(sample);
    const guardPos, const guardDir, var obstacles, const bounds = try parse(std.testing.allocator, stream.reader());
    defer obstacles.deinit();

    try std.testing.expectEqual(Point{ .x = 4, .y = 6 }, guardPos);
    try std.testing.expectEqual(Point{ .x = 10, .y = 10 }, bounds);
    try std.testing.expectEqual(.north, guardDir);

    try std.testing.expectEqual(41, try part1(std.testing.allocator, guardPos, guardDir, obstacles, bounds));
    try std.testing.expectEqual(6, try part2(std.testing.allocator, guardPos, guardDir, obstacles, bounds));
}
