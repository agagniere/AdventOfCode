const std = @import("std");

pub fn main() !void {
    var part1: u32 = 0;
    var part2: u32 = 0;

    for (2..7) |a| {
        for (a..10) |b| {
            for (b..10) |c| {
                for (c..10) |d| {
                    for (d..10) |e| {
                        for (e..10) |f| {
                            const n = 10 * (10 * (10 * (10 * (10 * a + b) + c) + d) + e) + f;
                            if (n > 235741) {
                                if (a == b or b == c or c == d or d == e or e == f) {
                                    part1 += 1;
                                }
                                if ((a == b and b != c) or (a != b and b == c and c != d) or (b != c and c == d and d != e) or (c != d and d == e and e != f) or (d != e and e == f)) {
                                    part2 += 1;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    std.debug.print("Number of possible passwords                : {:5}\n", .{part1});
    std.debug.print("Number of possible passwords with extra rule: {:5}\n", .{part2});
}
