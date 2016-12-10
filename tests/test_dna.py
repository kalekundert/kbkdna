#!/usr/bin/env python2

import pytest
import kbkdna

def test_reverse_complement():
    assert kbkdna.reverse_complement('ATGC') == 'GCAT'

def test_gc_content():
    assert kbkdna.gc_content('ATGC') == 0.5

