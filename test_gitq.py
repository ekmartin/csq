import gitq
import random
import wikiquote
# import subprocess


def test_humans_quote():
    """Should be able to retrieve a quote from all humans in HUMANS"""
    for human in gitq.HUMANS:
        print("Testing Human : {}".format(human))
        random.choice(wikiquote.quotes(human))
