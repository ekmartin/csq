import gitq
import json
import wikiquote


def write_quotes():
    """Quotes from HUMANS saved to quotes.txt"""
    quotes = {}
    for human in gitq.HUMANS:
        quotes[human] = wikiquote.quotes(human, max_quotes=150)
    with open('quotes.txt', 'w') as f:
        json.dump(quotes, f, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    write_quotes()
