#!/usr/bin/env python3

#It takes the FASTA sequences and translates them into proteins, stopping at the first stop codon.

#!/usr/bin/env python3
import os
from Bio.Seq import Seq
from Bio import SeqIO

if __name__ == "__main__":
    # Obtener la carpeta donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fasta_file = os.path.join(script_dir, "../data/example.fasta")

    for record in SeqIO.parse(fasta_file, "fasta"):
        dna_seq = Seq(str(record.seq))
        
        # Ajustar secuencia al múltiplo de 3 para evitar la advertencia
        seq_len = len(dna_seq) - len(dna_seq) % 3
        dna_seq = dna_seq[:seq_len]

        protein_seq = dna_seq.translate(to_stop=True)
        print(f"{record.id}: {protein_seq}")

