"""gitq

Usage:
    gitq quote <name>
    gitq [--version]

Arguments:
  name              Name of person to quote

Options:
  -h --help         Show help
  -v --version      Show version
"""
import sys
import docopt
import random
import wikiquote


if __name__ == "__main__":
    args = docopt.docopt(__doc__, argv=sys.argv[1:])
    if args['quote']:
        name = args['<name>']
        quote = random.choice(wikiquote.quotes(name))
        print(name, quote, sep=" -> ")
