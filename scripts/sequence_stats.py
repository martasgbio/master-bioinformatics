#!/usr/bin/env python3

#Calculate the length of each sequence and the GC content, and how many times each nucleotide appears.
import os
from Bio import SeqIO
from collections import Counter

def gc_content(seq):
    """Calculate GC content (%) of a DNA sequence."""
    gc_count = seq.count("G") + seq.count("C")
    return round((gc_count / len(seq)) * 100, 2)

def nucleotide_counts(seq):
    """Return a dictionary with counts of each nucleotide."""
    return dict(Counter(seq))

if __name__ == "__main__":
    # Get the folder where the script is located.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq)
        length = len(seq)
        gc = gc_content(seq)
        counts = nucleotide_counts(seq)
        
        print(f"Sequence ID: {record.id}")
        print(f"Length: {length}")
        print(f"GC Content: {gc}%")
        print(f"Nucleotide counts: {counts}")
        print("-" * 40)

