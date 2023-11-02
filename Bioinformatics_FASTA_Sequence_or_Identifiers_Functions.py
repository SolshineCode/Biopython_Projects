# Licensed and publicly released under https://firstdonoharm.dev/version/3/0/bds-cl-eco-extr-ffd-law-media-mil-my-sv-tal.txt

# pip install biopython
from Bio import SeqIO

import os
from Bio import SeqIO

Config = {
    "filename": "data/sequences.fasta"
}

# Read the sequences from the FASTA file
def read_fasta_file():
    with open(Config["filename"], "r") as file:
        sequences = [str(record.seq) for record in SeqIO.parse(file, "fasta")]
    return sequences

# Read the identifiers from the FASTA file
def read_fasta_identifiers():
    with open(Config["filename"], "r") as file:
        identifiers = [record.id for record in SeqIO.parse(file, "fasta")]
    return identifiers
