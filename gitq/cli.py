"""
Usage:
    gitq quote
    gitq [--version]
    gitq [--enable]

Arguments:
  quote             A computer related quote

Options:
  -h --help         Show help
  -v --version      Show version
  -e --enable       Enable gitq in the current Git repository
"""

import gitq
import gitq.quote_formatter
import docopt


def main(args=None):
    """CLI entry point to the program"""
    args = docopt.docopt(__doc__, argv=args)

    if args['quote']:
        q, p = gitq.quote_formatter.get_quote()
        q, p = gitq.quote_formatter.format_quote(q, p)
        print(q)
        print(p)
    elif args['--version']:
        print(gitq.VERSION)
    else:
        print(__doc__)
