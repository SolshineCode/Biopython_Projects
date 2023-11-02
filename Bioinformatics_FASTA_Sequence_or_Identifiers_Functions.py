# pip install biopython
from Bio import SeqIO

Config = {
    filename: # fill in filename here ie "data/sequences.fasta"
}

# Read the sequences from the FASTA file
def read_fasta_file(filename):
    with open(filename, "r") as file:
        sequences = [str(record.seq) for record in SeqIO.parse(file, "fasta")]
    return sequences

# Read the identifiers from the FASTA file
def read_fasta_identifiers(filename):
    with open(filename, "r") as file:
        identifiers = [record.id for record in SeqIO.parse(file, "fasta")]
    return identifiers
