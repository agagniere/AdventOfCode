const std = @import("std");
const Point3D = @import("point.zig").Point3D;
const Node = @import("graph.zig").Node;

const Allocator = std.mem.Allocator;
const Reader = std.Io.Reader;

pub fn parse(alloc: Allocator, input: *Reader) ![]Node {
    var result: std.ArrayList(Node) = try .initCapacity(alloc, 512);
    defer result.deinit(alloc);

    while (try input.takeDelimiter('\n')) |line| {
        try result.append(alloc, .{ .pos = try parse_line(line) });
    }
    return result.toOwnedSlice(alloc);
}

fn parse_line(line: []const u8) !Point3D {
    var token = std.mem.tokenizeScalar(u8, line, ',');
    const x = try std.fmt.parseInt(u32, token.next().?, 10);
    const y = try std.fmt.parseInt(u32, token.next().?, 10);
    const z = try std.fmt.parseInt(u32, token.next().?, 10);
    return .init(x, y, z);
}
