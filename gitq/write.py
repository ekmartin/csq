import json
import wikiquote

OFFSET = 79
VERSION = '0.0.1'
INDENT_OFFSET = 4

HUMANS = [
    'Donald Knuth',  'Tim Berners-Lee', 'Alan Turing', 'Grace Hopper',
    'Ada Lovelace', 'Ken Thompson', 'Niklaus Wirth', 'John von Neumann',
    'Dennis Ritchie', 'Brian Kernighan', 'Edsger W. Dijkstra', 'Larry Wall',
    'Linus Torvalds', 'John Backus', 'Richard Stallman', 'Bjarne Stroustrup',
    'Douglas Crockford'
]


def write_quotes():
    """Quotes from HUMANS saved to quotes.txt"""
    quotes = {}
    for human in HUMANS:
        quotes[human] = wikiquote.quotes(human, max_quotes=150)
    with open('quotes.txt', 'w') as f:
        json.dump(quotes, f, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    write_quotes()
