#!/usr/bin/env python2

def reverse(seq):
    return seq[::-1]

def complement(seq):
    complements = str.maketrans('ACTGactg', 'TGACtgac')
    return seq.translate(complements)

def reverse_complement(seq):
    return reverse(complement(seq))

def gc_content(seq):
    # This function contain a bug...
    return sum(x in 'GC' for x in seq) / len(seq)

