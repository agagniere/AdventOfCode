const std = @import("std");
const utils = @import("utils");

const Allocator = std.mem.Allocator;
const Stack = std.ArrayListUnmanaged(*Trie);

const Color = enum(u3) {
    white,
    blue,
    black,
    red,
    green,

    pub fn from_char(c: u8) ?Color {
        return switch (c) {
            'w' => .white,
            'u' => .blue,
            'b' => .black,
            'r' => .red,
            'g' => .green,
            else => null,
        };
    }
};

const Trie = struct {
    is_leaf: bool,
    children: [5]?*Trie,

    const empty: Trie = .{ .is_leaf = false, .children = .{null} ** 5 };

    pub fn insert(self: *Trie, allocator: Allocator, word: []const u8) !void {
        if (word.len == 0) {
            self.is_leaf = true;
        } else {
            const color = @intFromEnum(Color.from_char(word[0]).?);
            if (self.children[color] == null) {
                self.children[color] = try allocator.create(Trie);
                self.children[color].?.* = Trie.empty;
            }
            try self.children[color].?.insert(allocator, word[1..]);
        }
    }
};

const Solver = struct {
    root: *const Trie,
    cache: std.StringHashMap(u64),

    pub fn init(allocator: Allocator, towels: *const Trie) Solver {
        return .{ .root = towels, .cache = std.StringHashMap(u64).init(allocator) };
    }

    pub fn count(self: *Solver, word: []const u8) Allocator.Error!u64 {
        if (self.cache.get(word)) |res| {
            return res;
        }
        const res = try self._count(self.root, word);
        try self.cache.put(word, res);
        return res;
    }

    fn _count(self: *Solver, current: *const Trie, word: []const u8) !u64 {
        var result: u64 = 0;

        if (word.len == 0) {
            return if (current.is_leaf) 1 else 0;
        }
        const color = @intFromEnum(Color.from_char(word[0]).?);
        if (current.is_leaf) {
            result += try self.count(word);
        }
        if (current.children[color]) |child| {
            result += try self._count(child, word[1..]);
        }
        return result;
    }
};

fn parseFirstLine(allocator: Allocator, line: []const u8) !Trie {
    var root: Trie = Trie.empty;
    var towelIterator = std.mem.splitSequence(u8, line, ", ");

    while (towelIterator.next()) |towel| {
        try root.insert(allocator, towel);
    }
    return root;
}

pub fn main() !void {
    var gpa: std.heap.GeneralPurposeAllocator(.{}) = .{};
    defer _ = gpa.deinit();

    var arena = std.heap.ArenaAllocator.init(gpa.allocator());
    defer arena.deinit();
    var stdin = std.io.bufferedReader(std.io.getStdIn().reader());

    var lines = utils.lineIteratorSize(3000, stdin.reader());
    const towels = try parseFirstLine(arena.allocator(), lines.next().?);
    var solver = Solver.init(gpa.allocator(), &towels);
    defer solver.cache.deinit();

    var part1: u32 = 0;
    var part2: u64 = 0;

    _ = lines.next();
    while (lines.next()) |line| {
        const ways = try solver.count(line);
        std.log.debug("{s:<20} {}", .{ line, ways });
        if (ways > 0)
            part1 += 1;
        part2 += ways;
        solver.cache.clearRetainingCapacity();
    }
    std.debug.print("Number of possible patterns: {}\n", .{part1});
    std.debug.print("Number of arrangements:      {}\n", .{part2});
}
