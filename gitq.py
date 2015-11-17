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
import textwrap


if __name__ == "__main__":
    args = docopt.docopt(__doc__, argv=sys.argv[1:])
    if args['quote']:
        name = args['<name>']

        quote_selection = wikiquote.quotes(name, max_quotes=100)
        single_quote = random.choice(quote_selection)

        wrapped_quote = '\n'.join(textwrap.wrap(single_quote, 80))
        wrapped_indented_quote = textwrap.indent(wrapped_quote, '   ')

        print(name, wrapped_indented_quote, sep='\n')
