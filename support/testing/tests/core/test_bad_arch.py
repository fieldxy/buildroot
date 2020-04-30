import infra
import infra.basetest
import subprocess


class DetectBadArchTest(infra.basetest.BRConfigTest):
    config = infra.basetest.BASIC_TOOLCHAIN_CONFIG + infra.basetest.MINIMAL_CONFIG
    br2_external = [infra.filepath("tests/core/br2-external/detect-bad-arch")]

    def test_run(self):
        with self.assertRaises(SystemError):
            self.b.build()
        logf_path = infra.log_file_path(self.b.builddir, "build",
                                        infra.basetest.BRConfigTest.logtofile)
        if logf_path:
            s = 'ERROR: architecture for "/usr/bin/foo" is "Advanced Micro Devices X86-64", should be "ARM"'
            logf = open(logf_path, "r")
            ret = subprocess.call(["grep", "-q", s], stdin=logf)
            self.assertEqual(ret, 0)
