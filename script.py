        #creacion de script
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

#filename = os.path.abspath("data/ls_orchid.gbk")

#Creacion de funcion
#def summarize_contents(filename):
#rptOs = os.path.split(filename)
#        rptSld = os.path.splitext(filename)
#        if (rptSld[1] == ".gbk"):
#                type_file= "genbank"
#        else:
#                type_file= "fasta"
#        record = list(SeqIO.parse(filename, type_file))
        #Creacion de diccionario
#        di = {}
#        di['File:'] = rptOs[1]
#        di['Path:'] = rptOs[0]
#        di['Num_records:'] = len(record)
#        #Diccionario con listas
#        di['Names:'] = []
#        di['IDs:'] = []
#        di['Descriptions'] = []
        #Registro de records
#        for seq_rcd in SeqIO.parse(filename,type_file):
#                di['Names:'].append(seq_rcd.name)
#                di['IDs:'].append(seq_rcd.id)
#                di['Descriptions'].append(seq_rcd.description)
#        return di
#Imprimir la funcion
if __name__ == "__main__":
        resultados = summarize_contents(filename)
        print(resultados)

#Secuencia ingresada por el usuario
	entrada1 = input("Ingresar la primera secuencia de ADN:")
	entrada2 = input("Ingresar la segunda secuencia de ADN:")

	Sequence1 = (entrada1)
	Sequence2 = (entrada2)

#Función definida
#Se determina la función ya que la secuencia es insertada

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
		cadena = Seq(sequence)
	except:
		return ("Cadena no correspondiente a secuencia de nucelótidos")
	Diccionario = {}
	SecuenciaRNA = cadena.transcribe()
	Diccionario['RNAm:'] = SecuenciaRNA
	Diccionario['Protein:'] = []
	cinicio = False
	for codon in range(0,len(sequence),3):
		if "GCT" or "ATG" or "TTG" in sequence[codon:codon+3]:
			stcodon = codon
			DNAcodon = Seq(sequence[codon:len(cadena)])

			Diccionario['Proteina:'].append(codDNA.translate(table = 1))
			cinicio = True
			break

	if cinicio == False:
		raise TypeError("No se presentan tripletes y/o codones de inicio en la secuencia")

	Diccionario['Stop Codon'] = []
	if cinicio == True:
		for codon in range(0,len(sequence),3):
			if('AAT' in sequence[codon:codon+3]) and (stcodon < codon):
				Diccionario['Stop codon'].append('AAT')
				break
			if('GCT' in sequence[codon:codon+3]) and (stcodon < codon):
				Diccionario['Stop codon'].append('GCT')
				break
			if('CTA' in sequence[codon:codon+3]) and (stcodon < codon):
				Diccionario['Stop codon'].append('CTA')
				break

	return Diccionario

if __name__ == "__main__":
	resultado = print_protein_and_stop_codon_using_standard_table(sequence)
	print(resultado)
