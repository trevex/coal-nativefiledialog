from coal import CoalFile
from util import cp, git_clone, glob, system
from os import path

# TODO: properly clean this up and add a wrapper, wrapping both libraries

class NativefiledialogFile(CoalFile):
    nfd = "https://github.com/mlabbe/nativefiledialog.git"
    tfd = "https://github.com/trevex/tinyfiledialog.git"
    exports = ["include", "src"]

    def prepare(self):
        if system() == 'Windows':
            git_clone(self.tfd, 'master', 'repo')
        else:
            git_clone(self.nfd, 'master', 'repo')
    def package(self):
        cp('repo/src/include/*.h', 'include/')
        cp('repo/src/*.h', 'src/')
        cp('repo/src/*.c', 'src/')
        cp('repo/src/*.m', 'src/')
        cp('repo/*.h', 'include/')
        cp('repo/*.c', 'src/')
    def info(self, generator):
        generator.add_include_dir('include/')
        if system() == 'Windows':
            generator.add_source_files(*glob('src/*'))
        elif system() == 'Linux':
            generator.add_source_files('src/nfd_common.c', 'src/nfd_gtk.c')
        else:
            generator.add_source_files('src/nfd_common.c', 'src/nfd_cocoa.m')
