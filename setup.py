import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='gitq',
    version='0.0.1',
    author='Luke Murphy',
    author_email='lukewm@riseup.net',
    description='@TODO',
    license='@TODO',
    keywords='git',
    url='@TODO',
    packages=find_packages(exclude='tests'),
    long_description=read('README.md'),
    install_requires=[
        'lxml',
        'docopt',
        'wheel',
        'wikiquote'
    ],
    entry_points={
        'console_scripts': ['gitq=gitq.gitq:main']
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
