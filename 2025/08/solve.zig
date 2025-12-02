const std = @import("std");
const Point3D = @import("point.zig").Point3D;

const Allocator = std.mem.Allocator;
const Reader = std.Io.Reader;

pub fn day08(alloc: Allocator, input: *Reader) struct { u64, u64 } {
    return solve(alloc, input) catch unreachable;
}
pub fn solve(alloc: Allocator, input: *Reader) !struct { u64, u64 } {
    var timer: std.time.Timer = try .start();

    const jboxes = try parse(alloc, input);
    defer alloc.free(jboxes);
    const tp = timer.lap();

    var links = try build_edges(alloc, jboxes);
    defer links.deinit();
    const te = timer.lap();

    const p1 = try part1(alloc, &links);
    const t1 = timer.lap();

    std.log.info("[08] parse: {D}, ~{D}/line", .{ tp, tp / jboxes.len });
    std.log.info("[08] prepare: {D}, ~{D}/link", .{ te, te / links.capacity() });
    std.log.info("[08] part1: {D}", .{t1});
    return .{ p1, 0 };
}

fn part1(alloc: Allocator, links: *LinksByClosest) !u64 {
    const limit: usize = if (links.count() < 1000) 10 else 1000;
    var groups: std.ArrayList(std.ArrayList(*Node)) = .empty;
    defer groups.deinit(alloc);
    defer for (groups.items) |*group| group.deinit(alloc);

    for (0..limit) |_| {
        const link = links.remove();

        if (link.a.group) |cA| {
            if (link.b.group) |cB| {
                if (cA == cB)
                    continue;
                try groups.items[cA].ensureUnusedCapacity(alloc, groups.items[cB].items.len);
                groups.items[cA].appendSliceAssumeCapacity(groups.items[cB].items);
                for (groups.items[cB].items) |prev| {
                    prev.group = cA;
                }
                groups.items[cB].clearAndFree(alloc);
            } else {
                link.b.group = cA;
                try groups.items[cA].append(alloc, link.b);
            }
        } else if (link.b.group) |cB| {
            link.a.group = cB;
            try groups.items[cB].append(alloc, link.a);
        } else {
            link.a.group = @intCast(groups.items.len);
            link.b.group = @intCast(groups.items.len);
            try groups.append(alloc, try .initCapacity(alloc, 2));
            groups.items[link.a.group.?].appendSliceAssumeCapacity(&.{ link.a, link.b });
        }
    }
    var groupSize: std.ArrayList(usize) = try .initCapacity(alloc, groups.items.len);
    defer groupSize.deinit(alloc);
    for (groups.items) |group| {
        if (group.items.len > 0) {
            groupSize.appendAssumeCapacity(group.items.len);
        }
    }
    std.sort.block(usize, groupSize.items, {}, std.sort.desc(usize));
    return groupSize.items[0] * groupSize.items[1] * groupSize.items[2];
}

const Node = struct {
    pos: Point3D,
    group: ?u32 = null,
};

const Link = struct {
    length_squared: i64,
    a: *Node,
    b: *Node,
};

fn compare_links(_: void, a: Link, b: Link) std.math.Order {
    return if (a.length_squared < b.length_squared)
        .lt // smaller distance => higher priority
    else if (a.length_squared > b.length_squared)
        .gt // bigger distance => lower priority
    else
        .eq;
}

const LinksByClosest = std.PriorityQueue(Link, void, compare_links);

// Tested building the min-heap iteratively and found
// significantly worse performance that heapifying it at the end
fn build_edges(alloc: Allocator, boxes: []Node) !LinksByClosest {
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

fn parse_line(line: []const u8) !Point3D {
    var token = std.mem.tokenizeScalar(u8, line, ',');
    const x = try std.fmt.parseInt(u32, token.next().?, 10);
    const y = try std.fmt.parseInt(u32, token.next().?, 10);
    const z = try std.fmt.parseInt(u32, token.next().?, 10);
    return .init(x, y, z);
}

fn parse(alloc: Allocator, input: *Reader) ![]Node {
    var result: std.ArrayList(Node) = try .initCapacity(alloc, 512);
    defer result.deinit(alloc);

    while (try input.takeDelimiter('\n')) |line| {
        try result.append(alloc, .{ .pos = try parse_line(line) });
    }
    return result.toOwnedSlice(alloc);
}
