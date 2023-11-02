# Biopython_Projects

Licensed under Hippocratic License with select modules as detailed in "license" in repo and here: https://firstdonoharm.dev/version/3/0/bds-cl-eco-extr-ffd-law-media-mil-my-sv-tal.txt

# 1. FASTA Sequence and Identifier reader functions file

Bioinformatics FASTA Sequence and Identifiers Functions
This repository contains Python functions for reading sequences and identifiers from a FASTA file using the BioPython library. The code was inspired by a challenge from the YouTube video "Bioinformatics How to read FASTA files with Python and Biopython Tutorial" by Bioinformatics 101.

Functions
The repository includes two main functions:

read_fasta_file(filename): This function takes a filename as an argument, opens the file in read mode, and uses the SeqIO.parse function from BioPython to parse the file as a FASTA file. It then creates a list of the sequences in the file and returns this list.

read_fasta_identifiers(filename): This function works similarly to read_fasta_file, but instead of extracting the sequences, it extracts the identifiers of the sequences. The identifiers are then returned as a list.

Usage
To use these functions, you need to install BioPython. You can do this with pip:

Then, you can import the functions from the script and use them in your code:

Replace "path_to_your_file.fasta" with the path to the FASTA file you want to read.

Credits
Credit for the inspiration to create these functions goes to Bioinformatics 101. Check out their YouTube channel for more bioinformatics tutorials and challenges.

