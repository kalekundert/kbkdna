``kbkdna`` --- Simple tools for working with DNA
================================================
When doing biology, sometimes you just need to quickly know how long a 
DNA sequence is, or what its reverse complement is.  There are lots of 
tools out there that can tell you these things, but they often do a 
lot more than that too and can be overkill for really quick questions.  
In contrast, this package provides an easy-to-use command-line app 
that's just designed to give simple answers to simple questions.

.. image:: https://img.shields.io/pypi/v/kbkdna.svg
   :target: https://pypi.python.org/pypi/kbkdna
.. image:: https://img.shields.io/pypi/pyversions/kbkdna.svg
   :target: https://pypi.python.org/pypi/kbkdna
.. image:: https://img.shields.io/travis/kalekundert/kbkdna.svg
   :target: https://travis-ci.org/kalekundert/kbkdna
.. image:: https://readthedocs.org/projects/kbkdna/badge/?version=latest
   :target: http://kbkdna.readthedocs.io/en/latest/

Installation
------------
You can install ``kbkdna`` from PyPI using ``pip``::

   $ pip install kbkdna

Usage
-----
The command-line application that gets installed is called ``dna``.  
You can use the ``--help`` flag to get information on the kinds of 
things it can calculate::

   $ dna --help

You can use the ``len`` command to get the length of a DNA sequence::

   $ dna len CATCTAATTCAACAAGAATT
   20

You can use the ``rc`` command to get the reverse complement of a DNA 
sequence::

   $ dna rc CATCTAATTCAACAAGAATT
   AATTCTTGTTGAATTAGATG

You can use the ``gc`` command to calculate the GC content of a DNA 
sequence::

   $ dna gc CATCTAATTCAACAAGAATT
   25.0%

