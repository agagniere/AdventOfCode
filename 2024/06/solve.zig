const std = @import("std");
const utils = @import("utils");

const PointSet = std.AutoArrayHashMapUnmanaged(Point, void);
const InitialSituation = std.meta.Tuple(&.{ Point, Cardinal, PointSet, Point });
const Allocator = std.mem.Allocator;
const OrientedPoint = std.meta.Tuple(&.{ Point, Cardinal });
const OrientedPointSet = std.AutoHashMapUnmanaged(OrientedPoint, void);

const Cardinal = enum(u2) {
    north,
    west,
    south,
    east,

    pub fn next(self: Cardinal) Cardinal {
        return @enumFromInt(@intFromEnum(self) +% 1);
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

const Guard = struct {
    position: Point,
    facing: Cardinal,
    patrolArea: Point,

    pub fn next(self: *Guard, obstacles: PointSet) ?OrientedPoint {
        const peek = self.position.neighbor(self.facing);
        if (!peek.isInBounds(self.patrolArea)) {
            return null;
        } else if (obstacles.contains(peek)) {
            self.facing = self.facing.next();
        } else {
            self.position = peek;
        }
        return .{ self.position, self.facing };
    }
};

pub fn parse(allocator: Allocator, input: anytype) !InitialSituation {
    var obstacles: PointSet = .empty;
    var guard: ?Point = null;
    var lines = utils.lineIterator(input);
    var bound_x: i32 = 0;
    var y: i32 = 0;

    while (lines.next()) |line| {
        bound_x = @intCast(line.len);
        for (line, 0..line.len) |c, x| {
            if (c == '#') {
                try obstacles.put(allocator, .{ .x = @intCast(x), .y = y }, {});
            } else if (c == '^') {
                guard = .{ .x = @intCast(x), .y = y };
            }
        }
        y += 1;
    }
    return .{ guard.?, Cardinal.north, obstacles, .{ .x = bound_x, .y = y } };
}

fn part1(allocator: Allocator, guard: Guard, obstacles: PointSet) !u64 {
    var visited: PointSet = .empty;
    defer visited.deinit(allocator);
    var patrol = guard;

    try visited.ensureTotalCapacity(allocator, @intCast(guard.patrolArea.x * guard.patrolArea.y));
    visited.putAssumeCapacity(guard.position, {});
    while (patrol.next(obstacles)) |pos| {
        visited.putAssumeCapacity(pos[0], {});
    }
    return visited.count();
}

fn part2(allocator: Allocator, guard: Guard, obstacles: PointSet) !u64 {
    var arena = std.heap.ArenaAllocator.init(allocator);
    defer arena.deinit();
    const alloc = arena.allocator();

    var pastStates: OrientedPointSet = .empty;
    var visited: PointSet = .empty;
    var possibleObstacle: PointSet = .empty;
    var altPastStates: OrientedPointSet = .empty;
    var altObstacles: PointSet = try obstacles.clone(alloc);

    const area: u32 = @intCast(guard.patrolArea.x * guard.patrolArea.y);
    var patrol = guard;
    var previous = guard.position;

    try pastStates.ensureTotalCapacity(alloc, area);
    try visited.ensureTotalCapacity(alloc, area);
    try altObstacles.ensureUnusedCapacity(alloc, 1);
    try altPastStates.ensureTotalCapacity(alloc, area);
    try possibleObstacle.ensureTotalCapacity(alloc, 2 * obstacles.count());

    pastStates.putAssumeCapacity(.{ guard.position, guard.facing }, {});
    visited.putAssumeCapacity(guard.position, {});
    while (patrol.next(obstacles)) |pos| {
        pastStates.putAssumeCapacity(pos, {});
        if (!std.meta.eql(previous, pos[0])) {
            if (!visited.contains(pos[0])) {
                var alternative = Guard{ .position = previous, .facing = pos[1].next(), .patrolArea = guard.patrolArea };
                altObstacles.putAssumeCapacity(pos[0], {});
                while (alternative.next(altObstacles)) |alt| {
                    if (pastStates.contains(alt) or altPastStates.contains(alt)) {
                        possibleObstacle.putAssumeCapacity(pos[0], {});
                        break;
                    }
                    altPastStates.putAssumeCapacity(alt, {});
                }
                altPastStates.clearRetainingCapacity();
                _ = altObstacles.swapRemove(pos[0]);
            }
            visited.putAssumeCapacity(pos[0], {});
            previous = pos[0];
        }
    }

    // for (0..@intCast(guard.patrolArea.y)) |y| {
    //     for (0..@intCast(guard.patrolArea.x)) |x| {
    //         const p = Point{ .x = @intCast(x), .y = @intCast(y) };
    //         if (obstacles.contains(p)) {
    //             std.debug.print("#", .{});
    //         } else if (possibleObstacle.contains(p)) {
    //             std.debug.print("O", .{});
    //         } else std.debug.print(".", .{});
    //     }
    //     std.debug.print("\n", .{});
    // }

    return possibleObstacle.count();
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());

    const guardPos, const guardDir, var obstacles, const bounds = try parse(allocator, stdin.reader());
    defer obstacles.deinit(allocator);
    const guard = Guard{ .position = guardPos, .facing = guardDir, .patrolArea = bounds };

    var timer = try std.time.Timer.start();
    std.debug.print("Number of cells visited : {:5}\n", .{try part1(allocator, guard, obstacles)});
    std.debug.print("{}\n", .{std.fmt.fmtDuration(timer.lap())});
    std.debug.print("Number of possible loops: {:5}\n", .{try part2(allocator, guard, obstacles)});
    std.debug.print("{}\n", .{std.fmt.fmtDuration(timer.lap())});
}

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
    defer obstacles.deinit(std.testing.allocator);

    try std.testing.expectEqual(Point{ .x = 4, .y = 6 }, guardPos);
    try std.testing.expectEqual(Point{ .x = 10, .y = 10 }, bounds);
    try std.testing.expectEqual(.north, guardDir);

    const guard = Guard{ .position = guardPos, .facing = guardDir, .patrolArea = bounds };

    try std.testing.expectEqual(41, try part1(std.testing.allocator, guard, obstacles));
    try std.testing.expectEqual(6, try part2(std.testing.allocator, guard, obstacles));
}

test "Bruh" {
    const sample =
        \\..#.............
        \\..............#.
        \\...#............
        \\........#.......
        \\................
        \\.......#.....#..
        \\................
        \\..^.............
    ;
    var stream = std.io.fixedBufferStream(sample);
    const guardPos, const guardDir, var obstacles, const bounds = try parse(std.testing.allocator, stream.reader());
    defer obstacles.deinit(std.testing.allocator);

    const guard = Guard{ .position = guardPos, .facing = guardDir, .patrolArea = bounds };

    try std.testing.expectEqual(33, try part1(std.testing.allocator, guard, obstacles));
    try std.testing.expectEqual(1, try part2(std.testing.allocator, guard, obstacles));
}
