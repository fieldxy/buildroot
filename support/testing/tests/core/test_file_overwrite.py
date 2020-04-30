import infra
import infra.basetest
import subprocess


class DetectTargetFileOverwriteTest(infra.basetest.BRConfigTest):
    config = \
        infra.basetest.BASIC_TOOLCHAIN_CONFIG + \
        infra.basetest.MINIMAL_CONFIG + \
        """
        BR2_PER_PACKAGE_DIRECTORIES=y
        BR2_PACKAGE_DETECT_OVERWRITE=y
        """
    br2_external = [infra.filepath("tests/core/br2-external/detect-overwrite")]

    def test_run(self):
        with self.assertRaises(SystemError):
            self.b.build()
        logf_path = infra.log_file_path(self.b.builddir, "build",
                                        infra.basetest.BRConfigTest.logtofile)
        if logf_path:
            s = './etc/passwd: FAILED'
            logf = open(logf_path, "r")
            ret = subprocess.call(["grep", "-q", s], stdin=logf)
            self.assertEqual(ret, 0)


class DetectHostFileOverwriteTest(infra.basetest.BRConfigTest):
    config = \
        infra.basetest.BASIC_TOOLCHAIN_CONFIG + \
        infra.basetest.MINIMAL_CONFIG + \
        """
        BR2_PER_PACKAGE_DIRECTORIES=y
        BR2_PACKAGE_HOST_DETECT_OVERWRITE=y
        """
    br2_external = [infra.filepath("tests/core/br2-external/detect-overwrite")]

    def test_run(self):
        with self.assertRaises(SystemError):
            self.b.build()
        logf_path = infra.log_file_path(self.b.builddir, "build",
                                        infra.basetest.BRConfigTest.logtofile)
        if logf_path:
            s = './lib/pkgconfig/libpkgconf.pc: FAILED'
            logf = open(logf_path, "r")
            ret = subprocess.call(["grep", "-q", s], stdin=logf)
            self.assertEqual(ret, 0)
