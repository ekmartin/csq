import os
import io
import csq.cli
import subprocess
import csq.qformat
import collections


class TestCsqFormat:
    def test_indent(self):
        text = 'indent me'
        expected_length = len(text) + 4
        result = csq.qformat.indent(text)
        assert len(result) == expected_length

    def test_explode_quotes(self):
        quote_set = collections.OrderedDict((('a', [1, 2, 3]), ('b', [4, 5])))
        result = csq.qformat.explode_quote_set(quote_set)
        assert result == [(1, 'a'), (2, 'a'), (3, 'a'), (4, 'b'), (5, 'b')]

    def test_load_quotes(self):
        fpath = os.path.join(csq.BASE_DIR, 'quotes.txt')
        with io.open(fpath, encoding='utf-8') as fhandle:
            result = csq.qformat.load_quote_set(fhandle)
            assert isinstance(result, dict)


class TestCsqCLI:
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
