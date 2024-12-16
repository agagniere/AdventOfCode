const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{ .preferred_optimize_mode = .ReleaseFast });

    const utils = b.dependency("utils", .{ .target = target, .optimize = optimize }).module("utils");
    const coro = b.dependency("zigcoro", .{ .target = target, .optimize = optimize }).module("libcoro");

    const part1 = b.addExecutable(.{
        .name = "day7_1",
        .root_source_file = b.path("first.zig"),
        .target = target,
        .optimize = optimize,
    });
    const part2 = b.addExecutable(.{
        .name = "day7_2",
        .root_source_file = b.path("second.zig"),
        .target = target,
        .optimize = optimize,
    });

    part1.root_module.addImport("utils", utils);
    part2.root_module.addImport("utils", utils);
    part2.root_module.addImport("coroutines", coro);
    b.installArtifact(part1);
    b.installArtifact(part2);

    { // Test
        const test_step = b.step("test", "Run unit tests");
        const unit_tests = b.addTest(.{
            .root_source_file = b.path("first.zig"),
            .target = target,
            .optimize = optimize,
        });
        const run_unit_tests = b.addRunArtifact(unit_tests);

        unit_tests.root_module.addImport("utils", utils);
        test_step.dependOn(&run_unit_tests.step);
    }
    { // Test 2
        const test_step = b.step("test2", "Run unit tests of part 2");
        const unit_tests = b.addTest(.{
            .root_source_file = b.path("second.zig"),
            .target = target,
            .optimize = optimize,
        });
        const run_unit_tests = b.addRunArtifact(unit_tests);

        unit_tests.root_module.addImport("utils", utils);
        unit_tests.root_module.addImport("coroutines", coro);
        test_step.dependOn(&run_unit_tests.step);
    }
}
