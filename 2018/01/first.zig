const std = @import("std");

var buffered_in = std.io.bufferedReader(std.io.getStdIn().reader());
var source = buffered_in.reader();

const LineIterator = struct {
    buffer: [1024]u8 = undefined,

    pub fn next(self: *LineIterator) ?[]u8 {
        return source.readUntilDelimiterOrEof(&self.buffer, '\n') catch null;
    }
};

pub fn main() !void {
    var lines = LineIterator{};
    var total: i64 = 0;

    while (lines.next()) |line| {
        const value = std.fmt.parseInt(i32, line, 10) catch |err| {
            std.debug.print("Unable to parse into an int: {s}\n", .{line});
            return err;
        };
        total += value;
    }
    try std.fmt.format(std.io.getStdOut().writer(), "Resulting frequency: {}\n", .{total});
}
