import os

from conans import ConanFile, CMake, tools


class mFASTTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = ["boost/1.73.0"]
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            bin_path = os.path.join("bin", "message_printer")
            self.run(bin_path, run_environment=True)
