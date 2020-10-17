from Bio import SeqI0
from Bio.SeqRecord import SeqRecord
import os

# Archivo .gbk de mi escritorio, cambiar a la dirección del nuevo archivo .gbk a leer
filename = "/mnt/c/Users/danyarenee29/Desktop/Escritorio/comp/genome_assemblies_genome_gbk"

# Definición de la función summarize_contents
def summarize_contents(filename):
        lRuta = []
        lRuta = os.path.split(filename)
        print("file:", lRuta[1], "\npath:", lRuta[0]
        all_records=[]
        records = list(SeqI0.parse(filename, "genbank"))
        #print ("path: ", os.path.dirname(filename))
        print("num_records = %i records" % len(records))
        print("records:")
        for seq_record in SeqI0.parse(filename, "genbank"):
              all_records.append(seq_record.name)
              print("- id:",seq_record.id)
              print("name ",seq_record.name)
              print("description: ", seq_record.description)
              print("\n")
     
" Llamada a la función summarize_contents
  summarize_contents(filename)         
