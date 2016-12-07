#!/usr/bin/env python2

from __future__ import division

def reverse(seq):
    """Return the reverse of the given sequence (i.e. 3' to 
    5')."""
    return seq[::-1]

def complement(seq):
    """Return the complement of the given sequence (i.e. G=>C, 
    A=>T, etc.)"""
    from string import maketrans
    complements = maketrans('ACTGactg', 'TGACtgac')
    return seq.translate(complements)

def reverse_complement(seq):
    """Return the reverse complement of the given sequence 
    (e.g.  the opposite strand)."""
    return reverse(complement(seq))

# This function contains a bug.  Do you see it?
def gc_content(seq):
    """Return the GC content of the given sequence (e.g. the 
    fraction of nucleotides that are either G or C)."""
    return sum(x in 'GC' for x in seq) / len(seq)

