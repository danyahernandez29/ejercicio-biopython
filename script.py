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
     
# Llamada a la función summarize_contents
  summarize_contents(filename)         
#Secuencia ingresada por el usuario
sc1 = input("Ingresar la secuencia de ADN:")
sc2 = input("Ingresar la segunda secuencia de ADN:")

Sequence1 = Seq(s1)
Sequence2 = Seq(s2)

#Función definida
#Se determina la función ya que la secuencia es insertada

def concatenate_and_get_reverse_of_complement(Sequence1,Sequence2):
concatenate = Sequence1 + Sequence2 #serie de cadenas 
inverse = concatenate.reverse_complement()) 
return (concatenate.reverse_complement())

if _name__ == "_main_":
ressequence2 = concatenate_and_get_reverse_of_complement(Sequence1, Sequence2)
print(ressequence2) 
