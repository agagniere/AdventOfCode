const std = @import("std");

const Allocator = std.mem.Allocator;

fn number_of_digits(n: u64) u8 {
    return 1 + std.math.log10_int(n);
}

fn split(n: u64) ?[2]u64 {
    var exponent: u8 = 1;
    var power_of_ten: u64 = 10;
    var sep: u64 = 1;
    while (power_of_ten <= n) {
        exponent += 1;
        power_of_ten *= 10;
        if (exponent % 2 == 0)
            sep *= 10;
    }
    if (exponent % 2 != 0)
        return null;
    return .{ @divTrunc(n, sep), n % sep };
}

fn _how_many(blinks: u7, stone: u64) u64 {
    if (stone == 0) {
        return switch (blinks) {
            1, 2 => 1,
            else => how_many(blinks - 2, 2024),
        };
    }
    if (split(stone)) |pair| {
        return if (blinks == 1) 2 else how_many(blinks - 1, pair[0]) + how_many(blinks - 1, pair[1]);
    }
    return if (blinks == 1) 1 else how_many(blinks - 1, stone * 2024);
}

var cache: std.AutoHashMapUnmanaged(struct { u7, u64 }, u64) = .empty;

fn how_many(blinks: u7, stone: u64) u64 {
    if (cache.get(.{ blinks, stone })) |value| {
        return value;
    }
    const value = _how_many(blinks, stone);
    cache.putAssumeCapacity(.{ blinks, stone }, value);
    return value;
}

pub fn main() !void {
    const input = [_]u64{ 2, 77706, 5847, 9258441, 0, 741, 883933, 12 };
    const blinks = 75;
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const alloc = arena.allocator();

    try cache.ensureTotalCapacity(alloc, 140_000);

    var result: u64 = 0;
    var timer = try std.time.Timer.start();
    for (input) |stone| {
        result += how_many(blinks, stone);
    }
    const time = timer.read();
    std.debug.print("Number of stones after {} blinks: {}\n", .{ blinks, result });
    std.debug.print("{}\n", .{std.fmt.fmtDuration(time)});
    std.debug.print("cache entries: {}\n", .{cache.count()});
}
