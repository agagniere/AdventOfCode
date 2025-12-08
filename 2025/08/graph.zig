const std = @import("std");
const Point3D = @import("point.zig").Point3D;

const Allocator = std.mem.Allocator;

pub const Node = struct {
    pos: Point3D,
    group: ?u32 = null,
};

pub const Link = struct {
    length_squared: i64,
    a: *Node,
    b: *Node,
};

pub const LinksByClosest = std.PriorityQueue(Link, void, compare_links);

// Tested building the min-heap iteratively and found
// significantly worse performance that heapifying it at the end
pub fn build_edges(alloc: Allocator, boxes: []Node) !LinksByClosest {
    var result: std.ArrayList(Link) = try .initCapacity(alloc, boxes.len * boxes.len);
    defer result.deinit(alloc);

    for (0.., boxes[0 .. boxes.len - 1]) |i, *a| {
        for (boxes[i + 1 ..]) |*b| {
            result.appendAssumeCapacity(.{
                .a = a,
                .b = b,
                .length_squared = a.pos.distance_squared(b.pos),
            });
        }
    }
    return .fromOwnedSlice(alloc, try result.toOwnedSlice(alloc), {});
}

fn compare_links(_: void, a: Link, b: Link) std.math.Order {
    return if (a.length_squared < b.length_squared)
        .lt
    else if (a.length_squared > b.length_squared)
        .gt
    else
        .eq;
}
