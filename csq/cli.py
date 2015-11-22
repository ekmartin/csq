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
import csq.qformat


def main(args=None):
    """CLI entry point to the program"""
    args = docopt.docopt(__doc__, argv=args)

    if args['quote']:
        quote, person = csq.qformat.get_quote()
        print(
            csq.qformat.format_quote(quote),
            csq.qformat.format_person(person, len(quote))
        )
    elif args['--version']:
        print(csq.VERSION)
    else:
        print(__doc__)
