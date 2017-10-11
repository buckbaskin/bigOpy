#!/usr/bin/env python

import os
import re
import sys

from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand


packages = [
    'bigo',
]

requires = []
version = '0.0.1'

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='bigo',
    version=version,
    description='Circular Distributed job Queue',
    long_description=readme,
    author='William Baskin',
    url='http://github.com/buckbaskin/bigOpy',
    packages=packages,
    package_dir={'bigo': 'bigo'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
)

