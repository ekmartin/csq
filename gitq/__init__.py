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
import sys
import docopt
import random
import wikiquote
import textwrap

OFFSET = 79
VERSION = '0.0.1'
INDENT_OFFSET = 4

HUMANS = [
    'Donald Knuth', 'Tim Berners-Lee', 'Alan Turing', 'Grace Hopper',
    'Ada Lovelace', 'Ken Thompson', 'Niklaus Wirth', 'John von Neumann',
    'Dennis Ritchie', 'Brian Kernighan', 'Edsger W. Dijkstra', 'Larry Wall',
    'Linus Torvalds', 'John Backus', 'Richard Stallman', 'Bjarne Stroustrup',
    'Douglas Crockford'
]


def format_quote(quote, human):
    """Indented, annotated and wrapped quote and human name"""
    wrapped_quote = '\n'.join(textwrap.wrap(quote, OFFSET))
    fquote = textwrap.indent(wrapped_quote, ' '*INDENT_OFFSET)

    annotated_human = '|>> ' + human + ' <<|'
    human_offset = len(quote) if len(quote) < OFFSET else OFFSET
    indented_human = annotated_human.rjust(human_offset)
    fhuman = textwrap.indent(indented_human, ' '*INDENT_OFFSET)

    return fquote, fhuman


def get_quote():
    """A quote and a human who said it"""
    human = random.choice(HUMANS)
    quote_selection = wikiquote.quotes(human, max_quotes=100)
    single_quote = random.choice(quote_selection)
    return single_quote, human


def main():
    """CLI entry point to the program"""
    args = docopt.docopt(__doc__, argv=sys.argv[1:])

    if args['quote']:
        print(*format_quote(*get_quote()), sep='\n')
    elif args['--version']:
        print(VERSION)
    else:
        print(__doc__)
