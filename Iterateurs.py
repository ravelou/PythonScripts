class RevStr(str):
	def __iter__(self):
		return ItRevStr(self)

class ItRevStr:
	def __init__(self, chaine_a_parcourir):
		self.chaine_a_parcourir=chaine_a_parcourir
		self.position=len(self.chaine_a_parcourir)


	def __next__(self):
		if self.position==0:
			raise StopIteration
		self.position-=1
		return self.chaine_a_parcourir[self.position]


