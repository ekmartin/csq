import os
import gitq
import json
import random
import textwrap

OFFSET = 79
INDENT_OFFSET = 4


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
    with open(os.path.join(gitq.BASE_DIR, 'quotes.txt')) as f:
        quotes = json.load(f)
        human = random.choice(list(quotes.keys()))
        quote_selection = quotes[human]
        single_quote = random.choice(quote_selection)
        return single_quote, human
