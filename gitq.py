"""gitq

Usage:
    gitq quote
    gitq [--version]

Arguments:
  quote             A computer related quote

Options:
  -h --help         Show help
  -v --version      Show version
"""
import sys
import docopt
import random
import wikiquote
import textwrap

HUMANS = [
    'Donald Knuth', 'Tim Berners-Lee', 'Alan Turing', 'Grace Hopper',
    'Ada Lovelace', 'Ken Thompson', 'Niklaus Wirth', 'John von Neumann',
    'Dennis Ritchie', 'Brian Kernighan', 'Edsger W. Dijkstra', 'Larry Wall',
    'Linus Torvalds', 'John Backus', 'Richard Stallman', 'Bjarne Stroustrup',
    'Douglas Crockford'
]


def format_quote(quote):
    wrapped_quote = '\n'.join(textwrap.wrap(quote, 79))
    wrapped_indented_quote = textwrap.indent(wrapped_quote, '   ')
    return wrapped_indented_quote


def print_quote(quote, person):
    formatted_quote = format_quote(quote)

    offset = 79
    quote_length = len(formatted_quote)
    if quote_length < 79:
        offset = quote_length

    print(formatted_quote, person.rjust(offset), sep='\n\n')


def get_quote():
    person = random.choice(HUMANS)
    quote_selection = wikiquote.quotes(person, max_quotes=100)
    single_quote = random.choice(quote_selection)
    return single_quote, person

if __name__ == "__main__":
    args = docopt.docopt(__doc__, argv=sys.argv[1:])
    if args['quote']:
        quote, person = get_quote()
        print_quote(quote, person)
