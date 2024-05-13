"""
Importing Required Libraries
In this assignment, we'll be using the Biopython package, and we need to import the necessary libraries. The following libraries will be utilized:
1. Bio.SeqIO: This library will be used to parse the downloaded FASTA file into an object of type "Seq." 
This will enable us to leverage the various methods and functions provided by the Biopython package for our 
convenience.
2. Bio.Blast: This contains NCBIWWW and NCBIXML library which is used to perform the BLAST and parse the 
XML file produced respectively.
"""
from Bio import SeqIO as sio
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

"""
Now we define the list for the PDC genes for which we want to perform the BLAST and a list which has the
names of result files to be given after performing the BLAST.
"""
PDC_genes=["PDC1.fasta","PDC5.fasta","PDC6.fasta","PDC2.fasta"]
organism = "Saccharomyces cerevisiae"
name_of_files=["BLAST With PDC1","BLAST With PDC5","BLAST With PDC6","BLAST With PDC2"]
counter=0

"""
Through these for loops we iterate over the PDC genes fasta files and extract the PDC sequence from them.
After extracting them we perform the BLAST of that PDC against all the Saccharomyces cerevisiae strains,
using the qblast() function and provide all the necessary attributes. 
After the BLAST finishes we write all the results into a XML file using the file handling in python.
This is repeated for all the PDC gene sequences.
"""
for gene in PDC_genes:
    sequence=str(next(sio.parse(gene,"fasta")).seq)
    handle = NCBIWWW.qblast("blastn", "nt",sequence, entrez_query=f"{organism}[Organism]")
    file_handle=open(name_of_files[counter]+".xml",'w')
    data=handle.read()
    file_handle.write(data)
    file_handle.flush()
    file_handle.close()
    counter=counter+1


"""
After performing the BLAST, now we start parsing each of the XML files we fetched using the NCBIXML library.
And print the desired information like the strain name, Accession number, Length of sequence, Alignment of
that strain with the PDC gene. 
The articles used for learning about these libraries are as follows:-
1. https://biopython.org/docs/1.75/api/Bio.Blast.NCBIWWW.html 
2. https://biopython.org/docs/1.75/api/Bio.Blast.NCBIXML.html
The first Link provided a brief documentation of the NCBIWWW library and its functions and about the 
function parameters.
The second Link contained info about the NCBIXML library and details about how to parse the XML result file
after fetching it from the NCBI BLAST.
"""
for file in name_of_files:
    file_name=file+".xml"
    print("-----------------DATA FOR "+file_name+"------------------------")
    print()
    records=NCBIXML.parse(open(file_name))
    for data in records:
        name_of_strain=data.descriptions[0].title.split(',')[0]
        print("Strain Name: "+name_of_strain)
        for sequences in data.alignments:
            print("---------Alignment----------")
            print("Accession:", sequences.accession)
            print("Length:", sequences.length)
            for hsp in sequences.hsps:
                print("E value:", hsp.expect)
                print(hsp.query[::])
                print(hsp.match[::])
                print(hsp.sbjct[::])

"""
The output files produced after running this script were: BLAST With PDC1.xml,BLAST With PDC5.xml,
BLAST With PDC6.xml,BLAST With PDC2.xml. 
These contained the info of BLAST with the corresonding PDC gene.
"""