const std = @import("std");
const builtin = @import("builtin");

const Allocator = std.mem.Allocator;
const Io = std.Io;

const DaySolver = *const fn (Allocator, *Io.Reader) struct { u64, u64 };

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
    var buffer_out: [4096]u8 = undefined;
    var standard_output = std.fs.File.stdout().writer(&buffer_out);
    const out: *std.Io.Writer = &standard_output.interface;
    defer out.flush() catch {};

    const year = Io.Dir.cwd();

    try out.writeAll("| Day | Input | Part 1 | Part 2 |\n");
    try out.writeAll("| --: | :---- | :----- | :----- |\n");

    const day_names = [_][]const u8{ "01", "08" };
    const solvers = [_]DaySolver{ day01, day08 };
    const inputs = [_][]const u8{ "sample.txt", "input.txt" };

    for (day_names, solvers) |day_name, solver| {
        const day = try year.openDir(io, day_name, .{});
        defer day.close(io);

        for (inputs) |input_name| {
            const file = try day.openFile(io, input_name, .{});
            defer file.close(io);

            var buffer_in: [4096]u8 = undefined;
            var reader = file.reader(io, &buffer_in);

            const p1, const p2 = solver(gpa, &reader.interface);
            try out.print("|{s}|{s}|{}|{}|\n", .{ day_name, input_name, p1, p2 });
        }
    }
}

const day01 = @import("01/solve.zig").day01;
const day08 = @import("08/solve.zig").day08;
