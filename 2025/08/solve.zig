const std = @import("std");
const parse = @import("parse.zig").parse;
const build_edges = @import("graph.zig").build_edges;
const part1 = @import("part1.zig").part1;

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
