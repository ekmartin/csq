import gitq
import random
import wikiquote
import subprocess


class TestGitqInternals:
    def test_humans_quote(self):
        """Should be retrieve a quote from all humans in gitq.HUMANS"""
        for human in gitq.HUMANS:
            random.choice(wikiquote.quotes(human))


class TestGitqCLI:
    def strip_stdout(self, s):
        return s.replace('\n', '')

    def test_docopt_string(self):
        """Should return docstring when calling `gitq` without arguments"""
        args = ['gitq']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.__doc__) == self.strip_stdout(r1)

    def test_docopt_string_with_short_help_arg(self):
        """Should return docstring when passing `-h` argument"""
        args = ['gitq', '-h']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.__doc__) == self.strip_stdout(r1)

    def test_docopt_string_with_long_help_arg(self):
        """Should return docstring when passing `--help` argument"""
        args = ['gitq', '--help']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.__doc__) == self.strip_stdout(r1)

    def test_long_version(self):
        """Should return version when passing `--version` argument"""
        args = ['gitq', '--version']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(r1) == gitq.VERSION

    def test_short_version(self):
        """Should return version when passing `quote` argument"""
        args = ['gitq', '-v']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(r1) == gitq.VERSION

    def test_quote(self):
        """Should return quote when passing `quote` argument"""
        args = ['gitq', 'quote']
        r1 = subprocess.check_output(args).decode()
        assert isinstance(r1, str)
        assert (delim in r1 for delim in ['|>>', '<<|'])

    def test_short_enable_fails(self):
        """Should return an error when no .git/ directory present and passing `-e` argument"""
        pass

    def test_short_enable_succeeeds(self):
        """Should add correct code to .git/post-commit and passing `-e` argument"""
        pass

    def test_long_enable_fails(self):
        """Should return an error when no .git/ directory present and passing `--enable` argument"""
        pass

    def test_long_enable_succeeeds(self):
        """Should add correct code to .git/post-commit when passing `--enable` argument"""
        pass
