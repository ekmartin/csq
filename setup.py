import os
import setuptools
import distutils.core


class PyTest(distutils.core.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setuptools.setup(
    name='gitq',
    version='0.0.1',
    author='Luke Murphy',
    author_email='lukewm@riseup.net',
    description='@TODO',
    license='@TODO',
    keywords='git',
    url='@TODO',
    packages=setuptools.find_packages(exclude='tests'),
    long_description='README.md',
    install_requires=[
        'lxml',
        'docopt',
        'wheel',
        'wikiquote'
    ],
    entry_points={
        'console_scripts': ['gitq=gitq:main']
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
    cmdclass={'test': PyTest}
)
