#!/usr/bin/env python2

import pytest
from kbkdna.dna import *

def test_reverse_complement():
    assert reverse_complement('ATGC') == 'GCAT'

def test_gc_content():
    assert gc_content('ATGC') == 0.5

