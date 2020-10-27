import unittest
import script
import os

#Creacion de clase
class Prueba(unittest.TestCase):
	def test_summarize_contents(self):
		d_1 = {'File:': 'AF323668.gbk', 'Path:': os.path.abspath('data'), 'Num_records:': 1, 'Names:': ['AF323668'], 'IDs:': ['AF323668.1'], 'Descriptions': ['Bacteriophage bIL285, complete genome']}
		s = script.summarize_contents(os.path.abspath("data/AF323668.gbk"))
		self.assertDictEqual(d_1, s)

		d_2 = {'File:': 'NC_002703.gbk', 'Path:': os.path.abspath('data'), 'Nu
