1. File Structure

The Code Files are:- Part-1.py, Part-2(a).py, Part-2(b).py, Part-3.py, utility.py
Part-1.py: It has the code to download the DNA sequence of the Saccharomyces cerevisiae PDC gene.
Part-2(a).py: It has the code to perform the BLAST with all the PDC genes downloaded in the Part-1.py.
Part-2(b).py: It performs a linear scan over the sequences and identify and reports the SNPs.
Part-3.py: It translates the normal and SNP-containing PDC gene sequences into amino acid sequences.
utility.py: It is not the part of assignment. I used it to find the changes in amino acid so that i can use PolyPhen.

Other Files:-
BLAST.pdf: It is a pdf document which contains the screenshots and explanation too of BLAST on NCBI website.
PolyPhen.pdf: It is a pdf document which contains the screenshots and explanation of PolyPhen, which i performed using the PolyPhen website.
BLAST With PDC-1.txt: It is a txt file which i downloaded after performing the BLAST using PDC-1 on the NCBI website. It has all the details which were displayed on the website in txt format. 
BLAST With Dots For Identities.txt: It is a txt file which i downloaded after performing the BLAST. It basically displays the Alignment of various strains of Saccharomyces Cerevisiae with the PDC-1 and if there's a dot then it indicates a similarity and if its not a dot then it is the base that has changed.

Code Output Files:- These files were produced as the output of the python codes.
BLAST With PDC1.xml: It was produced as the output by the Part-2(a). It has the BLAST results with PDC-1 as the input sequence.   
BLAST With PDC2.xml: It was produced as the output by the Part-2(a). It has the BLAST results with PDC-2 as the input sequence.
BLAST With PDC5.xml: It was produced as the output by the Part-2(a). It has the BLAST results with PDC-5 as the input sequence. 
BLAST With PDC6.xml: It was produced as the output by the Part-2(a). It has the BLAST results with PDC-6 as the input sequence. 
PDC1.fasta: It was produced as the output by the Part-1. It contains the gene sequence of the PDC-1 in fasta format.
PDC2.fasta: It was produced as the output by the Part-1. It contains the gene sequence of the PDC-2 in fasta format.
PDC5.fasta: It was produced as the output by the Part-1. It contains the gene sequence of the PDC-5 in fasta format.
PDC6.fasta: It was produced as the output by the Part-1. It contains the gene sequence of the PDC-6 in fasta format.
PDC1 Protein Sequence.txt: It was produced as the output by the Part-3. It has the translated amino acid sequence for the PDC1.
Saccharomyces Cerevisiae YJM996 Protein Sequence.txt: It was produced as the output by the Part-3. It has the translated amino acid sequence for the Saccharomyces Cerevisiae YJM996 strain.

Other fasta files:-
Saccharomyces cerevisiae YJM996.fasta: It has the nucleotide sequence for the Saccharomyces cerevisiae YJM996 strain.
Saccharomyces cerevisiae YJM1199.fasta: It has the nucleotide sequence for the Saccharomyces cerevisiae YJM1199 strain. 



2. I performed BLAST with the python and from the NCBI website as well. Python as well as the pdf document both are attached.

3. For the SNP analysis i did it for Saccharomyces cerevisiae YJM996 strain. The code is attached for the same in Part-3. I translated both the PDC1 and this strain into amino acid sequence using the translate function of SeqIO package.

4. For the PolyPhen tool i performed the SNP for the position 15, for which K was changed to S. (PDC1 & Saccharomyces cerevisiae YJM996 strain).

5. Refrences:-
i. NCBI website: https://www.ncbi.nlm.nih.gov/
ii. Dataset For Saccharomyces cerevisiae: https://www.ncbi.nlm.nih.gov/datasets/taxonomy/4932/
iii. NCBI BLAST website: https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome
iv. Code Documentation for NCBI BLAST: https://biopython.org/docs/1.75/api/Bio.Blast.NCBIWWW.html , https://biopython.org/docs/1.75/api/Bio.Blast.NCBIXML.html
v. PolyPhen website: http://genetics.bwh.harvard.edu/pph2/