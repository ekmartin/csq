csq: computing quotes on the command line
=========================================

Introduction
------------

If you're feeling bereft of inspiration, hook this tiny CLI tool into
your work flow and start feeling smarter instantly! Over 30 amazing
humans in computing with ~1000 quotes.

.. figure:: https://i.imgur.com/tZ77msA.gif
   :alt: GIF

   GIF
Installation
------------

Using `pip <https://pip.pypa.io/en/stable/installing/>`__, it's as
simple as:

::

    pip install csq

Usage
-----

::

    csq quote
    csq -h
    csq -v

Recommendations
---------------

You can add this to a ``.bashrc``, ``.zshrc``, or even drop it into a
``post-commit`` in your ``.git/hooks/`` folder.

Compatability
-------------

This tool has been tested to run with ``python 2.7`` and ``python 3.4``.

Contributing
------------

More quotes will be added as I find them. However, if you feel that
there are some missing quotes (which there definitely are!), *please*
feel free to `make a pull request <https://github.com/lwm/csq/pulls>`__,
you can find the current lists of quotes
`here <https://github.com/lwm/csq/blob/master/csq/quotes.txt>`__. Go
ahead and `fork this
repository <https://help.github.com/articles/fork-a-repo/>`__!

This tool is tested to run on ``python-2.7`` and ``python-3.4``, so you
will need those interpreters installed to run the tests with
`tox <https://codespeak.net/tox/>`__.

::

    git clone https://github.com/<your-username>/csq
    cd csq && mkvirtualenv csq-dev
    pip install -r requirements.txt
    pip install -e .  # install csq locally
    tox  # run the tests

Contact
-------

Please see my `personal website <http://lukemurphy.eu/>`__.

License
-------

Please see `LICENSE.txt <https://github.com/lwm/csq/blob/master/LICENSE.txt>`__
