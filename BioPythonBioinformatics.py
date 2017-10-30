#!/usr/bin/env python
#with biopython
import os, sys, re
from Bio.Seq import Seq

def main():

    dna_seq = raw_input('Type your DNA sequence: ')    
    calling_seq = Seq(dna_seq)
    DNA_seq = calling_seq.reverse_complement()
    print 'Reverse complement DNA: ',DNA_seq
    sys.exit()

if __name__=='__main__':
    main()




