import gitq
import random
import wikiquote
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
    human = random.choice(gitq.HUMANS)
    quote_selection = wikiquote.quotes(human, max_quotes=100)
    single_quote = random.choice(quote_selection)
    return single_quote, human
