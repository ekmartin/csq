import csq.cli
import subprocess


class TestcsqCLI:
    def strip_stdout(self, s):
        return s.replace('\n', '')

    def test_docopt_string(self):
        args = ['csq']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(csq.cli.__doc__) == self.strip_stdout(r1)

    def test_docopt_string_with_short_help_arg(self):
        args = ['csq', '-h']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(csq.cli.__doc__) == self.strip_stdout(r1)

    def test_docopt_string_with_long_help_arg(self):
        args = ['csq', '--help']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(csq.cli.__doc__) == self.strip_stdout(r1)

    def test_long_version(self):
        args = ['csq', '--version']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(r1) == csq.VERSION

    def test_short_version(self):
        args = ['csq', '-v']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(r1) == csq.VERSION

    def test_quote(self):
        args = ['csq', 'quote']
        assert 0 == subprocess.call(args)
