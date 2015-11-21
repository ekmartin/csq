"""
Usage:
    gitq quote
    gitq [--version]

Arguments:
  quote             A computing related quote

Options:
  -h --help         Show help
  -v --version      Show version
"""

import gitq
import docopt
from gitq.qformat import format_quote, get_quote


def main(args=None):
    """CLI entry point to the program"""
    args = docopt.docopt(__doc__, argv=args)

    if args['quote']:
        quote, person = format_quote(*get_quote())
        print(quote, person)
    elif args['--version']:
        print(gitq.VERSION)
    else:
        print(__doc__)
