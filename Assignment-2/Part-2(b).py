"""
Importing Required Libraries
In this assignment, we'll be using the Biopython package, and we need to import the necessary libraries. The following libraries will be utilized:
1. Bio.SeqIO: This library will be used to parse the downloaded FASTA file into an object of type "Seq." 
This will enable us to leverage the various methods and functions provided by the Biopython package for our 
convenience.
"""
from Bio import SeqIO as sio

"""
Here we declare a list containing the names of strains for which i analyzed the SNP.
I downloaded the fasta files corresponding to these from the NCBI BLAST and then parsed them here using 
the SeqIO parse() function. 
"""
list_of_genes=["Saccharomyces cerevisiae YJM996","Saccharomyces cerevisiae YJM1199"]
Saccharomyces_cerevisiae_PDC1=""
record=next(sio.parse("PDC1.fasta","fasta"))
Saccharomyces_cerevisiae_PDC1=str(record.seq)
total_snp=0

"""
Now to report a SNP, we just iterate over the two sequences and find whether at a particular position 
the bases are same or different. If they are different then we record the position and the base changed.
And finally we print all such changes.
"""
for gene in list_of_genes:
    print("SNPs Between PDC1 And "+gene+"..................................\n")
    for sequence_record in sio.parse(gene+".fasta","fasta"):
        Strain=str(sequence_record.seq)
        print("Positions Of SNPs are:-")
        for i in range(len(Saccharomyces_cerevisiae_PDC1)):
            if(Saccharomyces_cerevisiae_PDC1[i]!=Strain[i]):
                print(str(i+1)+" : "+Saccharomyces_cerevisiae_PDC1[i]+" ->"+" "+Strain[i])
                total_snp+=1
        print("Total SNPs: ",total_snp)
        print()
        total_snp=0