const std = @import("std");

const LineIterator = struct {
    buffer: [1024]u8 = undefined,
    file: std.fs.File = std.io.getStdIn(),
    pub fn next(self: *LineIterator) ?[]u8 {
        return self.file.reader().readUntilDelimiterOrEof(&self.buffer, '\n') catch {
            return null;
        };
    }
};

fn extractValue(line: []const u8) ?u8 {
    var numbers = std.ArrayList(u8).init(std.heap.page_allocator);
    defer numbers.deinit();

    for (line) |c| {
        if (std.ascii.isDigit(c)) {
            numbers.append(std.fmt.charToDigit(c, 10) catch 0) catch return null;
        }
    }
    return 10 * numbers.items[0] + numbers.getLast();
}

pub fn main() void {
    var result: u32 = 0;
    var lines = LineIterator{};
    while (lines.next()) |line| {
        result += extractValue(line) orelse 0;
    }
    std.fmt.format(std.io.getStdOut().writer(), "Sum: {}\n", .{result}) catch {};
}

test "Use the first and last digits" {
    try std.testing.expect(extractValue("12345") == 15);
    try std.testing.expect(extractValue("987654") == 94);
}

test "Ignore non digits" {
    try std.testing.expect(extractValue("toto8hello5lmao2ok") == 82);
    try std.testing.expect(extractValue("no7non4nine6nein") == 76);
}

test "Sample" {
    try std.testing.expect(extractValue("1abc2") == 12);
    try std.testing.expect(extractValue("pqr3stu8vwx") == 38);
    try std.testing.expect(extractValue("a1b2c3d4e5f") == 15);
    try std.testing.expect(extractValue("treb7uchet") == 77);
}
