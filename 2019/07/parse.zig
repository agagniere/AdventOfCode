const std = @import("std");
const utils = @import("utils");

const Allocator = std.mem.Allocator;
const NumberList = std.ArrayListUnmanaged(i64);

/// Read the source code from an input stream (in ASCII and base 10)
pub fn parse(allocator: Allocator, source_reader: anytype) ![]i64 {
    var words = utils.lineIteratorCustom(16, ',', source_reader);
    var program = try NumberList.initCapacity(allocator, 4096);

    while (words.next()) |word| {
        const trimmed = std.mem.trim(u8, word, "\n");
        try program.append(allocator, try std.fmt.parseInt(i64, trimmed, 10));
    }
    return program.toOwnedSlice(allocator);
}

test parse {
    const source = "3,15,3,16,1002,16";
    var stream = std.io.fixedBufferStream(source);
    const program = try parse(std.testing.allocator, stream.reader());
    defer std.testing.allocator.free(program);

    try std.testing.expectEqualSlices(i64, &.{ 3, 15, 3, 16, 1002, 16 }, program);
}
