csq: computing quotes on the command line
=========================================

.. image:: https://travis-ci.org/lwm/csq.svg
    :target: https://travis-ci.org/lwm/csq

.. image:: https://badge.fury.io/py/csq.svg
    :target: https://badge.fury.io/py/csq

.. image:: https://landscape.io/github/lwm/csq/master/landscape.svg?style=flat
    :target: https://landscape.io/github/lwm/csq/master
    :alt: Code Health

Introduction
------------

If you're feeling bereft of inspiration, hook this tiny CLI tool into
your work flow and start feeling smarter instantly! Over 30 amazing
humans in computing with ~1000 quotes.

.. figure:: https://i.imgur.com/lAeN8vy.gif
   :alt: GIF

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

Compatibility
-------------

This tool has been tested to run with ``python 2.7`` and ``python 3.4``.

Contributing
------------

More quotes will be added as I find them. However, if you feel that
there are some missing quotes (which there definitely are!), *please*
feel free to `make a pull request <https://github.com/lwm/csq/pulls>`__,
you can find the current list of quotes
`here <https://github.com/lwm/csq/blob/master/csq/quotes.txt>`__.

You will need the ``2.7`` and ``3.4`` interpreters installed to run the tests with
`tox <https://codespeak.net/tox/>`__.

::

    git clone https://github.com/<your-username>/csq
    cd csq && mkvirtualenv csq-dev
    pip install -r requirements.txt
    pip install -e .  # install csq locally
    tox  # run the tests


It has been highlighted to me that this has some potential for a
`QOTD <https://en.wikipedia.org/wiki/QOTD>`__ service. So, that will
be a nice way to extend ``csq``.

Contact
-------

Please see my `personal website <http://lukemurphy.eu/>`__.

License
-------

Please see `LICENSE.txt <https://github.com/lwm/csq/blob/master/LICENSE.txt>`__
