import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="gitq",
    version="0.0.1",
    author="Luke Murphy",
    author_email="lukewm@riseup.net",
    description="@TODO",
    license="@TODO",
    keywords="git",
    url="@TODO",
    packages=['gitq', 'tests'],
    long_description=read('README.md'),
    classifiers=['@TODO'],
)
