from bio.seq import seq
from bio.seqFeature import seqFeature, FeatureLocation
from Bio import seqRecord
def summarize_contents(filename):
        a = SeqIO.read(filename, "genbank")
        print("Name: ", a.name)
        import os
        print ("Path: ", os.path.dirname(filename))
        b = list(SeqIO.parse(filename, "genbank"))
        print("num_records = %i records" % len(b))

        for seq_a in SeqIO.parse(filename,"genbank"):
                print("ID:",a.id)
         
summarize_contents(filename)
