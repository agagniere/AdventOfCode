const std = @import("std");

pub const Point3D = struct {
    value: V,

    const T = i64;
    const V = @Vector(3, T);

    pub fn init(x: T, y: T, z: T) Point3D {
        return .{ .value = .{ x, y, z } };
    }

    pub fn module_squared(self: Point3D) T {
        const square = self.value * self.value;
        return @reduce(.Add, square);
    }

    pub fn distance_squared(self: Point3D, other: Point3D) T {
        const diff: Point3D = .{ .value = self.value - other.value };
        return diff.module_squared();
    }
};

test Point3D {
    const a: Point3D = .init(1, 2, 3);
    try std.testing.expectEqual(14, a.module_squared());

    const b: Point3D = .init(3, 2, -1);
    try std.testing.expectEqual(14, b.module_squared());
    try std.testing.expectEqual(20, a.distance_squared(b));
    try std.testing.expectEqual(20, b.distance_squared(a));
}
