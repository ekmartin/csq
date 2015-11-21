"""
Usage:
    csq quote
    csq [--version]

Arguments:
  quote             A computing related quote

Options:
  -h --help         Show help
  -v --version      Show version
"""
from __future__ import print_function

import csq
import docopt
from csq.qformat import format_quote, get_quote


def main(args=None):
    """CLI entry point to the program"""
    args = docopt.docopt(__doc__, argv=args)

    if args['quote']:
        quote, person = format_quote(*get_quote())
        print(quote, person)
    elif args['--version']:
        print(csq.VERSION)
    else:
        print(__doc__)
