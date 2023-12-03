const std = @import("std");

var buffered_in = std.io.bufferedReader(std.io.getStdIn().reader());
var source = buffered_in.reader();

const LineIterator = struct {
    buffer: [1024]u8 = undefined,

    pub fn next(self: *LineIterator) ?[]u8 {
        return source.readUntilDelimiterOrEof(&self.buffer, '\n') catch null;
    }
};

fn asIntArrayList(comptime T: type, lines: *LineIterator) !std.ArrayList(T) {
    var result = try std.ArrayList(T).initCapacity(std.heap.page_allocator, 1000);

    while (lines.next()) |line| {
        const value = std.fmt.parseInt(T, line, 10) catch {
            std.debug.print("Unable to parse into an int: {s}\n", .{line});
            continue;
        };
        result.append(value) catch break;
    }
    return result;
}

fn findDuplicate(changes: std.ArrayList(i32)) !i64 {
    var frequency: i64 = 0;
    var seen = std.AutoHashMap(i64, bool).init(std.heap.page_allocator);

    while (true) {
        for (changes.items) |change| {
            if (seen.contains(frequency)) {
                return frequency;
            }
            try seen.put(frequency, true);
            frequency += change;
        }
    }
}

pub fn main() !void {
    var iterator = LineIterator{};
    const changes = try asIntArrayList(i32, &iterator);
    defer changes.deinit();

    const duplicate: i64 = try findDuplicate(changes);

    try std.fmt.format(std.io.getStdOut().writer(), "Repeated frequency: {}\n", .{duplicate});
}
