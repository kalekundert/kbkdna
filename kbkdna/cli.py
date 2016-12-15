#!/usr/bin/env python2

"""\
Perform various simple manipulations on DNA sequences.

Usage:
    dna len <seq>
    dna rc <seq>
    dna gc <seq> [--fraction]

Commands:
    len:  Print the length of the given DNA sequence.
    rc:   Print the reverse-complement of the given DNA sequence.
    gc:   Print the GC content of the given DNA sequence.

Arguments:
    <seq>:  The DNA sequence to work with.

Options:
    --fraction 
        For the 'gc' command, display the result as a raw fraction
        (e.g. a number between 0 and 1) rather than a percentage.
"""

from . import dna

def main():
    import docopt
    args = docopt.docopt(__doc__)
    seq = args['<seq>']

    if args['len']:
        print len(seq)
    if args['rc']:
        print dna.reverse_complement(seq)
    if args['gc']:
        gc = dna.gc_content(seq)
        if args['--fraction']: print gc
        else: print '{:.2f}%'.format(gc / 100.)

