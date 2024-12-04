const std = @import("std");
const utils = @import("utils");

const PositionedLetter = std.AutoHashMap(Point, u8);
const Allocator = std.mem.Allocator;

const Point = struct {
    x: i32,
    y: i32,

    pub fn add(self: Point, other: Point) Point {
        return .{ .x = self.x + other.x, .y = self.y + other.y };
    }

    pub fn corners(self: Point) CornerIterator {
        return .{ .center = self };
    }
};

/// Loop over the 8 possible directions
const directions: [8]Point = blk: {
    var result: [8]Point = undefined;

    for (0..9) |i| {
        result[i - (if (i > 4) 1 else 0)] = .{ .x = (@as(i32, i) % 3) - 1, .y = @as(i32, i) / 3 - 1 };
    }
    break :blk result;
};

/// Infinite iteration from a point in a given direction
const RayIterator = struct {
    current: Point,
    move: Point,

    pub fn next(self: *RayIterator) ?Point {
        self.current = self.current.add(self.move);
        return self.current;
    }
};

/// Iterate over the 4 corners of a given point
const CornerIterator = struct {
    center: Point,
    index: u8 = 0,

    const corners: [4]Point = .{
        .{ .x = -1, .y = -1 },
        .{ .x = 1, .y = -1 },
        .{ .x = 1, .y = 1 },
        .{ .x = -1, .y = 1 },
    };

    pub fn next(self: *CornerIterator) ?Point {
        if (self.index == 4)
            return null;
        const current = self.center.add(corners[self.index]);
        self.index += 1;
        return current;
    }
};

/// Build the hashmap from an iterator of lines
pub fn parse(allocator: Allocator, input: anytype) !PositionedLetter {
    var result = PositionedLetter.init(allocator);
    var lines = utils.lineIterator(input);
    var y: i32 = 0;

    while (lines.next()) |line| {
        for (line, 0..line.len) |c, x| {
            try result.put(.{ .x = @intCast(x), .y = y }, c);
        }
        y += 1;
    }
    return result;
}

pub fn part1(input: PositionedLetter) u32 {
    var iter = input.iterator();
    var result: u32 = 0;

    while (iter.next()) |letter| {
        if (letter.value_ptr.* == 'X') {
            for (directions) |direction| {
                var ray: RayIterator = .{ .current = letter.key_ptr.*, .move = direction };
                var i: u32 = 0;

                while (ray.next()) |p| {
                    if (input.get(p) orelse break != "MAS"[i])
                        break;
                    i += 1;
                    if (i > 2) {
                        result += 1;
                        break;
                    }
                }
            }
        }
    }
    return result;
}

pub fn part2(input: PositionedLetter) u32 {
    var iter = input.iterator();
    var result: u32 = 0;

    outer: while (iter.next()) |letter| {
        if (letter.value_ptr.* == 'A') {
            var corners = letter.key_ptr.corners();
            var surroundings: [4]u8 = undefined;
            var i: u32 = 0;

            while (corners.next()) |corner| {
                const c = input.get(corner) orelse continue :outer;
                surroundings[i] = c;
                i += 1;
            }
            if (std.mem.indexOf(u8, "MSSMMSS", &surroundings) != null) {
                result += 1;
            }
        }
    }
    return result;
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());

    var input = try parse(allocator, stdin.reader());
    defer input.deinit();

    std.debug.print("Number of 'XMAS' : {:5}\n", .{part1(input)});
    std.debug.print("Number of X 'MAS': {:5}\n", .{part2(input)});
}

// -------------------- Tests --------------------

test part1 {
    const sample =
        \\MMMSXXMASM
        \\MSAMXMSMSA
        \\AMXSXMAAMM
        \\MSAMASMSMX
        \\XMASAMXAMM
        \\XXAMMXXAMA
        \\SMSMSASXSS
        \\SAXAMASAAA
        \\MAMMMXMMMM
        \\MXMXAXMASX
    ;
    var stream = std.io.fixedBufferStream(sample);
    var input = try parse(std.testing.allocator, stream.reader());
    defer input.deinit();

    try std.testing.expectEqual(18, part1(input));
    try std.testing.expectEqual(9, part2(input));
}
