"""
Importing Required Libraries
In this assignment, we'll be using the Biopython package, and we need to import the necessary libraries. The following libraries will be utilized:
Bio.Entrez: This library will be used to connect to the NCBI database.
"""
from Bio import Entrez as ent

"""
Providing Email and Accession Number
To connect to the NCBI database, we need to provide our email for authentication purposes. 
"""
emailID = "nikhilkumar190804@gmail.com"
ent.email=emailID

"""
Additionally, we define a list of accession numbers that we will be using for this assignment.
This specific accession number will serve as the identifier to fetch the corresponding FASTA file.
Along with this we also define a list for the start and end positions of these particular genes and a value
for every gene to tell whether to download its reverse complement or not.
"""
PDC_gene_assession_numbers=["NC_001144.5","NC_001144.5","NC_001139.9","NC_001136.10"]
name_of_pdc_gene=["PDC1","PDC5","PDC6","PDC2"]
starting=[232390,  410723,651290,607304]
ending=[234081, 412414, 652981,610081]
isReversed=[True,False,True,True]

"""
Utilizing the efetch() Function from the Entrez Module
Now, we employ the efetch() function from the Entrez Module. This function is designed to retrieve a specific file in a specified format from the NCBI database using the provided accession number along with 
some extra attributes for start and end postions and for reverse complement form.
"""

"""
File Handling to Create a FASTA File
Using Python's file handling capabilities, we proceed to create a FASTA file. The `open()` function is employed for this purpose, and we write the data fetched by the handle into the file. This step completes the process of downloading the PDC gene sequences.
"""

"""
LINK FOR REFERENCE: https://www.ncbi.nlm.nih.gov/datasets/taxonomy/4932/
This Link had all the gene sequences corresponding to the Saccharomyces cerevisiae.
"""

for i in range(len(PDC_gene_assession_numbers)):
    accession_number=PDC_gene_assession_numbers[i]
    start=starting[i]
    end=ending[i]
    name_of_gene=name_of_pdc_gene[i]
    toBeReversed=isReversed[i]
    strand_value=1
    if(toBeReversed==True):
        strand_value=2
    handle = ent.efetch(db="nucleotide",id=accession_number,rettype="fasta",retmode="text",seq_start=start, seq_stop=end,strand=strand_value)
    record = handle.read()
    file = open(name_of_gene+".fasta",'w')
    file.write(record)
    file.flush()
    file.close()

"""
After running this script the files produced are: PDC1.fatsa,PDC5.fasta,PDC6.fasta,PDC2.fasta.
"""