        #creacion de script
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

#filename = os.path.abspath("data/ls_orchid.gbk")

#Function creation
def summarize_contents(filename):
rptOs = os.path.split(filename)
        rptSld = os.path.splitext(filename)
        if (rptSld[1] == ".gbk"):
                type_file= "genbank"
        else:
                type_file= "fasta"
        record = list(SeqIO.parse(filename, type_file))
        #Creacion de diccionario
        di = {}
        di['File:'] = rptOs[1]
        di['Path:'] = rptOs[0]
        di['Num_records:'] = len(record)
        #String dictionary
        di['Names:'] = []
        di['IDs:'] = []
        di['Descriptions'] = []
        #Records
        for seq_rcd in SeqIO.parse(filename,type_file):
                di['Names:'].append(seq_rcd.name)
                di['IDs:'].append(seq_rcd.id)
                di['Descriptions'].append(seq_rcd.description)
        return di
#Print function
if __name__ == "__main__":
        results = summarize_contents(filename)
        print(results)

#Sequence given my the user
	entry1 = input("Ingresar la primera secuencia de ADN:")
	entry2 = input("Ingresar la segunda secuencia de ADN:")

	Sequence1 = (entry1)
	Sequence2 = (entry2)

#Defined function
#Function is determined once the string is completed

def concatenate_and_get_reverse_of_complement(Sequence1,Sequence2):
	concatenate = Sequence1 + Sequence2 #serie de cadenas 
	inverse = concatenate.reverse_complement()) 
	return (concatenate.reverse_complement())

if __name__ == "__main__":
	ressequence2 = concatenate_and_get_reverse_of_complement(Sequence1, Sequence2)
	print(resSequence2)
=======
sequence = 'AGCTATACGACTCAG'
def print_protein_and_stop_codon_using_standard_table(sequence):
	try:
		string = Seq(sequence)
	except:
		return ("String not related to the nucleotide sequence")
	Diccionario = {}
	SequenceRNA = string.transcribe()
	Libraries['RNAm:'] = SequenceRNA
	Libraries['Protein:'] = []
	cstart = False
	for codon in range(0,len(sequence),3):
		if "GCT" or "ATG" or "TTG" in sequence[codon:codon+3]:
			stcodon = codon
			DNAcodon = Seq(sequence[codon:len(cadena)])

			Library['Protein:'].append(codDNA.translate(table = 1))
			cstart = True
			break

	if cstart == False:
		raise TypeError("No triplets and/or start codon found in the sequence")

	Library['Stop Codon'] = []
	if cstart == True:
		for codon in range(0,len(sequence),3):
			if('AAT' in sequence[codon:codon+3]) and (stcodon < codon):
				Library['Stop codon'].append('AAT')
				break
			if('GCT' in sequence[codon:codon+3]) and (stcodon < codon):
				Library['Stop codon'].append('GCT')
				break
			if('CTA' in sequence[codon:codon+3]) and (stcodon < codon):
				Library['Stop codon'].append('CTA')
				break

	return Library

if __name__ == "__main__":
	result = print_protein_and_stop_codon_using_standard_table(sequence)
	print(result)

#Extract_sequences function
narchivo = "/mnt/c/Users/danya/Videos/bioinfo/ejercio-biopyhton/data/sequences.fasta"
exit = "genbank"
tmolecule = "protein"
def extract_sequences(narchivo,exit):
    files = 0
    if(exit == "genbank"):
        SeqIO.convert(narchive, "fasta", "sequences.gbk", "genbank", tmolecule)
        records = list(SeqIO.parse("sequences.gbk","genbank"))
        for i, record in enumerate(records):
            f = open(f"sequence{i}.gbk", "w")
            f.write(record.format("genbank"))
            f.close()
            files = files+1
    else:
        records = list(SeqIO.parse(narchive,"fasta"))
        files = 0
        for i, record in enumerate(records): 
            f = open(f"sequence{i}.fasta", "w")
            f.write(record.format("fasta"))
            f.close()
            files = files+1
    return(files)
extract_sequences(narchive,exit)
