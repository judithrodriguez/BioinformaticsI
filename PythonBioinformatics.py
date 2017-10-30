#!/usr/bin/env python
#withoutBiopython

import os, sys, re

def reverse(s):
    sequence_list = []
    for base in s:
        sequence_list.append(base)
    reverse_seq_LIST = sequence_list[::-1]
    reverse_seq = ''.join(reverse_seq_LIST)
    return reverse_seq

def complement(s):
    sequence_list = []
    for base in s:
        if base == 'A':
            sequence_list.append('T')
        elif base == 'T':
            sequence_list.append('A')
        elif base == 'G':
            sequence_list.append('C')
        elif base == 'C':
            sequence_list.append('G')
    complement_seq = ''.join(sequence_list)
    return complement_seq

def main():
    DNA_Bases = ['A','G','T','C']
    correct_DNA = False
    while not correct_DNA:
        dna_seq = raw_input('Type your DNA sequence: ')
        dna_seq = dna_seq.upper()
        correct_DNA = True
        for base in dna_seq:
            if base not in DNA_Bases:
                correct_DNA = False
        if correct_DNA == False:
            print '** Error: Not a DNA sequence'

    reverse_DNA = reverse(dna_seq)
    dna_seq =complement(reverse_DNA)
    print 'Reverse complement DNA: ',dna_seq
    sys.exit()

if __name__=='__main__':
    main()

