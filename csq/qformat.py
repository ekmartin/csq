import io
import os
import csq
import json
import random
import textwrap

OFFSET = 65
INDENT_OFFSET = 4


def indent(text):
    """Indented text using 'INDENT_OFFSET'"""
    return '\n'.join((' '*INDENT_OFFSET) + x for x in text.splitlines())


def format_person(person, quote_len):
    """Offset and indented person"""
    person = '|>> ' + person + ' <<|'
    offset = quote_len if quote_len < OFFSET else OFFSET
    return indent('\n' + person.rjust(offset))


def format_quote(quote):
    """Wrapped, offset and indented quote"""
    wrapped_quote = '\n'.join(textwrap.wrap(quote, OFFSET))
    return indent(wrapped_quote)


def explode_quote_set(quote_set):
    """Transforms a dict of {k:[v]} to a list of [(k,v), (k,v)]"""
    return [
        (quote, person)
        for person in quote_set
        for quote in quote_set[person]
    ]


def load_quote_set(fhandle):
    """A JSON loaded fhandle"""
    return json.load(fhandle)


def get_quote():
    """A quote and a person who said it"""
    fpath = os.path.join(csq.__pkginfo__.BASE_DIR, 'quotes.txt')
    with io.open(fpath, encoding='utf-8') as fhandle:
        all_quotes = explode_quote_set(load_quote_set(fhandle))
        quote, person = random.choice(all_quotes)
        return quote, person
