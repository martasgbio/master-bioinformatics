#!/usr/bin/env python3

#Calculate the reverse complementary sequence for each DNA sequence.Print the result showing the sequence ID, the original sequence, and the inverse complementary sequence.

import os
from Bio.Seq import Seq
from Bio import SeqIO

if __name__ == "__main__":
    # Obtener la carpeta donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    for record in SeqIO.parse(fasta_file, "fasta"):
        dna_seq = Seq(str(record.seq))
        rev_comp = dna_seq.reverse_complement()
        print(f"{record.id}: Original: {dna_seq} -> Reverse Complement: {rev_comp}")

