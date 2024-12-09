const std = @import("std");

const Allocator = std.mem.Allocator;
const FileList = std.ArrayListUnmanaged(File);

pub fn arithmeticSeries(start: u64, count: u64) u64 {
    return @divExact(count * (2 * start + count - 1), 2);
}

const File = struct {
    ID: u64 = 0,
    address: u64,
    size: u64,

    pub fn checksum(self: File) u64 {
        return self.ID * arithmeticSeries(self.address, self.size);
    }
};

fn checksum(files: []File) u64 {
    var result: u64 = 0;
    for (files) |file| {
        result += file.checksum();
    }
    return result;
}

fn parse(allocator: Allocator, line: []const u8) !struct { FileList, FileList } {
    var files = try FileList.initCapacity(allocator, @divFloor(line.len, 2) + 1);
    var freespaces = try FileList.initCapacity(allocator, @divFloor(line.len, 2));
    var address: u64 = 0;
    var size: u64 = 0;

    for (0..line.len, line) |i, c| {
        size = try std.fmt.charToDigit(c, 10);
        if (i % 2 == 0) {
            files.appendAssumeCapacity(.{ .address = address, .size = size, .ID = files.items.len });
        } else {
            freespaces.appendAssumeCapacity(.{ .address = address, .size = size });
        }
        address += size;
    }
    return .{ files, freespaces };
}

fn part1(files: []File, freespaces: []File) u64 {
    var result: u64 = 0;
    var left: usize = 0;
    var right: usize = files.len - 1;
    var free: usize = 0;
    var address: u64 = 0;

    while (left < right) {
        result += files[left].checksum();
        address += files[left].size;
        left += 1;
        while (true) {
            const consumed = @min(freespaces[free].size, files[right].size);
            result += File.checksum(.{ .address = address, .size = consumed, .ID = files[right].ID });
            address += consumed;
            files[right].size -= consumed;
            if (files[right].size == 0) {
                right -= 1;
            }
            freespaces[free].size -= consumed;
            if (freespaces[free].size == 0) {
                free += 1;
                break;
            }
        }
    }
    if (files[right].size > 0)
        result += files[right].checksum();
    return result;
}

fn part2(files: []File, freespaces: *FileList) u64 {
    var right = files.len - 1;

    while (right > 0) {
        for (0..freespaces.items.len, freespaces.items) |i, space| {
            if (space.size >= files[right].size) {
                if (space.address >= files[right].size)
                    break;
                files[right].address = space.address;
                freespaces.items[i].size -= files[right].size;
                if (freespaces.items[i].size == 0) {
                    _ = freespaces.orderedRemove(i);
                } else freespaces.items[i].address += files[right].size;
                break;
            }
        }
        right -= 1;
    }
    return checksum(files);
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());
    const input = try stdin.reader().readAllAlloc(allocator, 21_000);
    defer allocator.free(input);

    var timer = try std.time.Timer.start();
    var times: [3]u64 = .{ 0, 0, 0 };
    var files, var freespaces = try parse(allocator, input[0 .. input.len - 1]);
    defer files.deinit(allocator);
    defer freespaces.deinit(allocator);
    times[0] = timer.lap();

    const one = part1(files.items, freespaces.items);
    times[1] = timer.lap();
    const two = part2(files.items, &freespaces);
    times[2] = timer.lap();

    std.debug.print("Compacted filesystem checksum   : {:12}\n", .{one});
    std.debug.print("Unfragmented filesystem checksum: {:12}\n", .{two});
    std.debug.print("parse: {}, part1: {}, part2: {}\n", .{ std.fmt.fmtDuration(times[0]), std.fmt.fmtDuration(times[1]), std.fmt.fmtDuration(times[2]) });
}

// -------------------- Tests --------------------

test "part1" {}

test "part2" {}
