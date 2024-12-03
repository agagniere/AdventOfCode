const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const source_file = b.path("utils.zig");

    _ = b.addModule("utils", .{
        .root_source_file = source_file,
        .target = target,
        .optimize = optimize,
    });

    { // Test
        const test_step = b.step("test", "Run unit tests");

        const unit_tests = b.addTest(.{
            .root_source_file = source_file,
            .target = target,
            .optimize = optimize,
        });

        const run_unit_tests = b.addRunArtifact(unit_tests);
        test_step.dependOn(&run_unit_tests.step);
    }
}
