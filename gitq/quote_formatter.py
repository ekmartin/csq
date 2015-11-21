import os
import gitq
import json
import random
import textwrap

OFFSET = 79
INDENT_OFFSET = 4


def indent(text):
    """Indented text using 'INDENT_OFFSET'"""
    return '\n'.join((' '*INDENT_OFFSET) + x for x in text.splitlines())


def format_quote(quote, human):
    """Indented and wrapped quote and human name"""
    formatted_quote = indent('\n'.join(textwrap.wrap(quote, OFFSET)))

    marked = '|>> ' + human + ' <<|'
    offset = len(quote) if len(quote) < OFFSET else OFFSET
    formatted_human = indent('\n' + marked.rjust(offset))

    return formatted_quote, formatted_human


def get_quote():
    """A quote and a human who said it"""
    with open(os.path.join(gitq.BASE_DIR, 'quotes.txt')) as f:
        quotes = json.load(f)
        human = random.choice(list(quotes.keys()))
        quote_selection = quotes[human]
        single_quote = random.choice(quote_selection)
        return single_quote, human
