"""
Importing Required Libraries
In this assignment, we'll be using the Biopython package, and we need to import the necessary libraries. The following libraries will be utilized:
1. Bio.SeqIO: This library will be used to parse the downloaded FASTA file into an object of type "Seq." This will enable us to leverage the various methods and functions provided by the Biopython package for our convenience.
2. Bio.Seq: This library has a class "Seq" which makes our work easier while dealing with long DNA sequences
"""
from Bio import SeqIO as sio
from Bio import Seq as s

"""
Here we declare a list to store the names of the output files.
"""
file_name=["PDC1 Protein Sequence","Saccharomyces Cerevisiae YJM996 Protein Sequence"]
counter=0

"""
This part of the code parses the nucleotide sequence of the strain and of PDC-1 gene and then simply
use the translate() function to convert that nucleotide sequence to the amino acid sequence.
After converting it, we use the file handling in python to store this translated sequence into a txt file
having a suitable name.
"""
for sequence_record in sio.parse("Saccharomyces cerevisiae YJM996.fasta","fasta"):
    newseq=sequence_record.seq
    with open(file_name[counter]+".txt",'w') as file:
        amino_acid_sequence=s.translate(newseq)
        file.write(str(amino_acid_sequence))
        file.close()
    counter+=1

"""
The output files produced after running this script were: PDC1 Protien Sequence,Saccharomyces Cerevisiae 
YJM996 Protein Sequence.txt
These contained the translated amino acid sequences of the corresponding sequence.
"""