#!/usr/bin/env python3

from distutils import setup

setup(
    name='kbkdna',
    version='0.0.0',
    author='Kale Kundert',
    author_email='kale.kundert@ucsf.edu',
    url='http://github.com/kalekundert/kbkdna',
    packages=[
        'kbkdna',
    ],
    install_requires=[
        'docopt',
    ],
    description='Simple tools for working with DNA',
    long_description=open('README.rst').read(),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)

