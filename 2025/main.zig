const std = @import("std");
const builtin = @import("builtin");

const Allocator = std.mem.Allocator;
const Io = std.Io;

pub fn main() !void {
    // Set up allocator.
    var debug_allocator: std.heap.DebugAllocator(.{}) = .init;
    defer std.debug.assert(debug_allocator.deinit() == .ok);
    const gpa = switch (builtin.mode) {
        .Debug, .ReleaseSafe => debug_allocator.allocator(),
        .ReleaseFast, .ReleaseSmall => std.heap.smp_allocator,
    };

    // Set up our I/O implementation.
    var threaded: std.Io.Threaded = .init(gpa);
    defer threaded.deinit();
    const io = threaded.io();

    return juicyMain(gpa, io);
}

pub fn juicyMain(gpa: Allocator, io: Io) !void {
    var buffer: [4096]u8 = undefined;
    var stdin = Io.File.stdin().reader(io, &buffer);
    std.log.info("Number of zeros: {}", .{try day01(gpa, &stdin.interface)});
}

const day01 = @import("01/first.zig").day01;
