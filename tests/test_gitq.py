import gitq
import random
import wikiquote
import subprocess


class TestGitqInternals:
    def test_humans_quote(self):
        """Should be able to retrieve a quote from all humans in HUMANS"""
        for human in gitq.HUMANS:
            random.choice(wikiquote.quotes(human))


class TestGitqCLI:
    def strip_stdout(self, s):
        return s.replace('\n', '')

    def test_docopt_string(self):
        """Should return docstring when gitq is called with no arguments"""
        args = ['gitq']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.__doc__) == self.strip_stdout(r1)

    def test_docopt_string_with_short_help_arg(self):
        """Should return docstring when gitq is called with short help arg"""
        args = ['gitq', '-h']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.__doc__) == self.strip_stdout(r1)

    def test_docopt_string_with_long_help_arg(self):
        """Should return docstring when gitq is called with long help arg"""
        args = ['gitq', '--help']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(gitq.__doc__) == self.strip_stdout(r1)

    def test_long_version(self):
        """Should return version when gitq is called with long version arg"""
        args = ['gitq', '--version']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(r1) == gitq.VERSION

    def test_short_version(self):
        """Should return version when gitq is called with short version arg"""
        args = ['gitq', '-v']
        r1 = subprocess.check_output(args).decode()
        assert self.strip_stdout(r1) == gitq.VERSION

    def test_quote(self):
        """Should return quote when gitq is called with quote argument"""
        args = ['gitq', 'quote']
        r1 = subprocess.check_output(args).decode()
        assert isinstance(r1, str)
        assert (delim in r1 for delim in ['|>>', '<<|'])
