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


def format_quote(quote, person):
    """Indented and wrapped quote and person"""
    person = '|>> ' + person + ' <<|'
    offset = len(quote) if len(quote) < OFFSET else OFFSET
    formatted_person = indent('\n' + person.rjust(offset))
    formatted_quote = indent('\n'.join(textwrap.wrap(quote, OFFSET)))
    return formatted_quote, formatted_person


def get_quote():
    """A quote and a person who said it"""
    with open(os.path.join(gitq.BASE_DIR, 'quotes.txt')) as fhandle:
        all_quotes = json.load(fhandle)
        person = random.choice(list(all_quotes.keys()))
        quote_selection = all_quotes[person]
        quote = random.choice(quote_selection)
        return quote, person
