        #creacion de script
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

filename = os.path.abspath("data/ls_orchid.gbk")

#Creacion de funcion
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
	#Diccionario con listas
	di['Names:'] = []
	di['IDs:'] = []
	di['Descriptions'] = []
	#Registro de records
	for seq_rcd in SeqIO.parse(filename,type_file):
		di['Names:'].append(seq_rcd.name)
		di['IDs:'].append(seq_rcd.id)
		di['Descriptions'].append(seq_rcd.description)
	return di
#Imprimir la funcion
if __name__ == "__main__":
	resultados = summarize_contents(filename)
	print(resultados)
