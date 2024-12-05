const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const libft = b.dependency("libft", .{ .target = target, .optimize = optimize }).artifact("ft");

    const exe = b.addExecutable(.{
        .name = "intcode",
        .target = target,
        .optimize = optimize,
    });
    exe.linkLibC();
    exe.addCSourceFile(.{ .file = b.path("solve.c"), .flags = &CFLAGS });
    exe.linkLibrary(libft);
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
}

const CFLAGS = .{
    "-Werror",
    "-Wall",
    "-Wextra",
    "-Wswitch",
    "-Wvla",
};
