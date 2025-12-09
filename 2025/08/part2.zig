const std = @import("std");
const graph = @import("graph.zig");

const Allocator = std.mem.Allocator;
const LinksByClosest = graph.LinksByClosest;
const Node = graph.Node;

pub fn part2(alloc: Allocator, links: *LinksByClosest, boxCount: usize, groups: *std.ArrayList(std.ArrayList(*Node))) !u64 {
    while (links.removeOrNull()) |link| {
        if (link.a.group) |cA| {
            if (link.b.group) |cB| {
                if (cA == cB)
                    continue;
                try groups.items[cA].appendSlice(alloc, groups.items[cB].items);
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
            try groups.append(alloc, .empty);
            try groups.items[link.a.group.?].appendSlice(alloc, &.{ link.a, link.b });
        }
        if (groups.items[link.a.group.?].items.len == boxCount)
            return @intCast(link.a.pos.value[0] * link.b.pos.value[0]);
    }
    unreachable;
}
