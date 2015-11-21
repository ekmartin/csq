import gitq.cli
import subprocess


class TestGitqCLI:
    def strip_stdout(self, s):
        return s.replace('\n', '')

    def test_docopt_string(self):
        args = ['gitq']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.cli.__doc__) == self.strip_stdout(r1)

    def test_docopt_string_with_short_help_arg(self):
        args = ['gitq', '-h']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.cli.__doc__) == self.strip_stdout(r1)

    def test_docopt_string_with_long_help_arg(self):
        args = ['gitq', '--help']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.cli.__doc__) == self.strip_stdout(r1)

    def test_long_version(self):
        args = ['gitq', '--version']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(r1) == gitq.VERSION

    def test_short_version(self):
        args = ['gitq', '-v']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(r1) == gitq.VERSION

    def test_quote(self):
        args = ['gitq', 'quote']
        r1 = subprocess.check_output(args).decode()
        assert isinstance(r1, str)
        assert (delim in r1 for delim in ['|>>', '<<|'])

    def test_short_enable_fails(self):
        pass

    def test_short_enable_succeeeds(self):
        pass

    def test_long_enable_fails(self):
        pass

    def test_long_enable_succeeeds(self):
        pass
