# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

def read():
    """Build a file path from *paths* and return the contents."""
    with codecs.open(os.path.join('README.rst'), 'r', "utf-8") as f:
        return f.read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import sys
        if sys.version_info[:2] == (2, 6):
            import unittest2 as unittest    # Python 2.6
        else:
            import unittest

        setup_file = sys.modules['__main__'].__file__
        setup_dir = os.path.abspath(os.path.dirname(setup_file))
        tests = unittest.TestLoader().discover(
            os.path.join(setup_dir, 'tests'), pattern='*.py')
        try:
            # https://github.com/CleanCut/green/issues/50
            from green.runner import run
            from green.suite import GreenTestSuite
            from green.config import default_args
            default_args.verbose = 3
            run(GreenTestSuite(tests), sys.stdout, default_args)
        except ImportError:
            unittest.TextTestRunner(verbosity=2).run(tests)


setup(
    name='loadcf',
    version='0.1.0',
    description='convert config file to python variable',
    long_description=read(),
    url='https://github.com/singpenguin/loadcf/',
    license='MIT',
    author='singpenguin',
    author_email='zhenjinglee@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'': ['README.md']},
    keywords=['config', 'JSON'],
    install_requires=[
    ],
    tests_require=['coverage'],
    extras_require={
        'coveralls': ['coveralls']
    },
    cmdclass={
        'test': PyTest,
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
