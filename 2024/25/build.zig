const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{ .preferred_optimize_mode = .ReleaseFast });

    const utils = b.dependency("utils", .{ .target = target, .optimize = optimize }).module("utils");

    const exe = b.addExecutable(.{
        .name = "day25",
        .root_source_file = b.path("first.zig"),
        .target = target,
        .optimize = optimize,
    });

    exe.root_module.addImport("utils", utils);
    b.installArtifact(exe);

    { // Run
        const run_step = b.step("run", "Run the app");
        const run_cmd = b.addRunArtifact(exe);

        run_cmd.step.dependOn(b.getInstallStep());
        if (b.args) |args| {
            run_cmd.addArgs(args);
        }
        run_step.dependOn(&run_cmd.step);
    }
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
}