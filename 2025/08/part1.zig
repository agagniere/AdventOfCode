const std = @import("std");
const graph = @import("graph.zig");

const Allocator = std.mem.Allocator;
const LinksByClosest = graph.LinksByClosest;
const Node = graph.Node;

pub fn part1(alloc: Allocator, links: *LinksByClosest) !u64 {
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
