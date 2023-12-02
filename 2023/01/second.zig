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

pub fn extractValue(line: []const u8) u8 {
    const spelled = std.ComptimeStringMap(u8, .{ .{ "one", 1 }, .{ "two", 2 }, .{ "three", 3 }, .{ "four", 4 }, .{ "five", 5 }, .{ "six", 6 }, .{ "seven", 7 }, .{ "eight", 8 }, .{ "nine", 9 } });
    var numbers = std.ArrayList(u8).init(std.heap.page_allocator);
    defer numbers.deinit();

    for (line, 0..) |c, i| {
        if (std.fmt.charToDigit(c, 10)) |digit| {
            numbers.append(digit) catch break;
        } else |_| for (3..6) |length| {
            if (length + i > line.len)
                break;
            if (spelled.get(line[i..][0..length])) |digit|
                numbers.append(digit) catch break;
        }
    }
    return 10 * numbers.items[0] + numbers.getLast();
}

pub fn main() void {
    var result: u32 = 0;
    var lines = LineIterator{};

    while (lines.next()) |line| {
        result += extractValue(line);
    }
    std.fmt.format(std.io.getStdOut().writer(), "Sum: {}\n", .{result}) catch {};
}

test "Still extract first and last simple digits" {
    try std.testing.expect(extractValue("12345") == 15);
    try std.testing.expect(extractValue("987654") == 94);
    try std.testing.expect(extractValue("toto8hello5lmao2ok") == 82);
    try std.testing.expect(extractValue("no7non4nine6nein") == 76);
}

test "Read numbers spelled out in letters" {
    try std.testing.expect(extractValue("nononosix7654seven3fourmis") == 64);
    try std.testing.expect(extractValue("wwtwo1one2eightxx") == 28);
}

test "Watch out for overlap" {
    try std.testing.expect(extractValue("oneight") == 18);
    try std.testing.expect(extractValue("twone") == 21);
    try std.testing.expect(extractValue("eightwo") == 82);
    try std.testing.expect(extractValue("threeight") == 38);
    try std.testing.expect(extractValue("fiveight") == 58);
    try std.testing.expect(extractValue("sevenine") == 79);
}

test "Sample" {
    try std.testing.expect(extractValue("two1nine") == 29);
    try std.testing.expect(extractValue("eightwothree") == 83);
    try std.testing.expect(extractValue("abcone2threexyz") == 13);
    try std.testing.expect(extractValue("xtwone3four") == 24);
    try std.testing.expect(extractValue("4nineeightseven2") == 42);
    try std.testing.expect(extractValue("zoneight234") == 14);
    try std.testing.expect(extractValue("7pqrstsixteen") == 76);
}
