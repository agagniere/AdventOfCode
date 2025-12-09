const std = @import("std");
const parse = @import("parse.zig").parse;
const part1 = @import("part1.zig").part1;
const part2 = @import("part2.zig").part2;
const graph = @import("graph.zig");

const Allocator = std.mem.Allocator;
const Reader = std.Io.Reader;

pub fn day08(alloc: Allocator, input: *Reader) struct { u64, u64 } {
    return solve(alloc, input) catch unreachable;
}

fn solve(alloc: Allocator, input: *Reader) !struct { u64, u64 } {
    var timer: std.time.Timer = try .start();

    const jboxes = try parse(alloc, input);
    defer alloc.free(jboxes);
    const tp = timer.lap();

    var links = try graph.build_edges(alloc, jboxes);
    defer links.deinit();
    var circuits: std.ArrayList(std.ArrayList(*graph.Node)) = try .initCapacity(alloc, jboxes.len >> 2);
    defer circuits.deinit(alloc);
    defer for (circuits.items) |*circuit| circuit.deinit(alloc);
    const te = timer.lap();

    const p1 = try part1(alloc, &links, &circuits);
    const plugged = links.capacity() - links.count();
    const t1 = timer.lap();

    const p2 = try part2(alloc, &links, jboxes.len, &circuits);
    const t2 = timer.lap();

    std.log.info("[08] parse: {D}, ~{D}/line", .{ tp, tp / jboxes.len });
    std.log.info("[08] prepare: {D}, ~{D}/link", .{ te, te / links.capacity() });
    std.log.info("[08] part1: {D}, ~{D}/conn", .{ t1, t1 / plugged });
    std.log.info("[08] part2: {D}, ~{D}/conn", .{ t2, t2 / (links.capacity() - links.count() - plugged) });
    return .{ p1, p2 };
}
