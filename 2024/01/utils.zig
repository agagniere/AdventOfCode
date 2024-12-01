const std = @import("std");

fn LineIterator(comptime size: usize, comptime readerType: type, comptime delimiter: u8) type {
    return struct {
        reader: readerType,
        buffer: [size]u8 = undefined,

        const Self = @This();

        pub fn next(self: *Self) ?[]u8 {
            return self.reader.readUntilDelimiterOrEof(&self.buffer, delimiter) catch {
                return null;
            };
        }
    };
}

/// Create an iterator from an infinite stream of bytes,
/// that yields each line encountered
pub fn lineIterator(reader: anytype) LineIterator(2048, @TypeOf(reader), '\n') {
    return .{ .reader = reader };
}

pub fn lineIteratorSize(comptime size: usize, reader: anytype) LineIterator(size, @TypeOf(reader), '\n') {
    return .{ .reader = reader };
}

pub fn lineIteratorCustom(comptime size: usize, comptime delimiter: u8, reader: anytype) LineIterator(size, @TypeOf(reader), delimiter) {
    return .{ .reader = reader };
}
