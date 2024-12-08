const std = @import("std");
const utils = @import("utils");

pub fn scan(input: []const u8) [2]u64 {
    var total: u64 = 0;
    var branched: u64 = 0;
    var enabled: bool = true;
    var state: enum { none, m, u, l, paren, term1, comma, term2, d, o, n, quote, t, dop, dontp } = .none;
    var left: u64 = 0;
    var right: u64 = 0;

    for (input) |c| {
        switch (state) {
            .none => {
                if (c == 'm')
                    state = .m;
                if (c == 'd')
                    state = .d;
            },

            .m => state = if (c == 'u') .u else .none,
            .u => state = if (c == 'l') .l else .none,
            .l => state = if (c == '(') .paren else .none,

            .paren => if (std.ascii.isDigit(c)) {
                left = c - '0';
                state = .term1;
            } else {
                state = .none;
            },

            .term1 => if (std.ascii.isDigit(c)) {
                left = left * 10 + (c - '0');
            } else if (c == ',') {
                state = .comma;
            } else {
                state = .none;
            },

            .comma => if (std.ascii.isDigit(c)) {
                right = c - '0';
                state = .term2;
            } else {
                state = .none;
            },

            .term2 => if (std.ascii.isDigit(c)) {
                right = right * 10 + (c - '0');
            } else if (c == ')') {
                total += left * right;
                if (enabled)
                    branched += left * right;
                state = .none;
            } else {
                state = .none;
            },

            .d => state = if (c == 'o') .o else .none,
            .o => state = if (c == '(') .dop else if (c == 'n') .n else .none,
            .n => state = if (c == '\'') .quote else .none,
            .quote => state = if (c == 't') .t else .none,
            .t => state = if (c == '(') .dontp else .none,

            .dop => {
                if (c == ')') enabled = true;
                state = .none;
            },
            .dontp => {
                if (c == ')') enabled = false;
                state = .none;
            },
        }
    }
    return .{ total, branched };
}

pub fn main() !void {
    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());
    var lines = utils.lineIteratorSize(3100, stdin.reader());
    var total: [2]u64 = .{ 0, 0 };
    var times: [2]u64 = .{ 0, 0 };
    var timer = try std.time.Timer.start();

    while (lines.next()) |line| {
        times[0] += timer.lap();
        const res = scan(line);
        total[0] += res[0];
        total[1] += res[1];
        times[1] += timer.lap();
    }
    std.debug.print("Program output: {:10}\n", .{total[0]});
    std.debug.print("With branching: {:10}\n", .{total[1]});
    std.debug.print("get next line: {}, part 1 & 2: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]) });
}

test "part1" {
    const sample = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";

    try std.testing.expectEqual(161, scan(sample)[0]);
}

test "part2" {
    const sample = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";

    try std.testing.expectEqual(48, scan(sample)[1]);
}
