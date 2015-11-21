import csq
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
        errno = subprocess.call([sys.executable, 'tests/runtests.py'])
        raise SystemExit(errno)


setuptools.setup(
    name='csq',
    version=csq.VERSION,
    author='Luke Murphy',
    author_email='lukewm@riseup.net',
    description='Computing quotes on the command line',
    license='GPL',
    keywords='git',
    url='https://github.com/lwm/csq',
    packages=setuptools.find_packages(exclude='tests'),
    long_description=open('README.md').read(),
    install_requires=[
        'docopt',
    ],
    entry_points={
        'console_scripts': ['csq=csq.__main__:main']
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ],
    cmdclass={'test': PyTest},
    package_data={
        'csq': ['quotes.txt'],
    },
)
