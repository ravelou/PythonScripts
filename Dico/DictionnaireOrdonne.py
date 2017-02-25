class DictionnaireOrdonne:
	def __init__(self,*arg,**parametres_nommes):
		"""constructeur de la classe"""
		self.cles=list()
		self.valeurs=list()
		
		if len(arg) > 0:
			for i,dual in enumerate(arg):
				if type(dual) is dict:
					for cle,valeur in dual.items():
						self.cles.append(cle)
						self.valeurs.append(valeur)
		elif len(parametres_nommes)>0:
			for cle,valeur in parametres_nommes.items():
				self.cles.append(cle)
				self.valeurs.append(valeur)
	
	def __del__(self):
		"""destructeur de la classe """
		del self.cles
		del self.valeurs

	def __repr__(self):
		"""affiche la classe quand on tape son nom sous forme de dictionnaire"""
		#dictionnaire=dict()
		chaine='{'
		for index,cle in enumerate(self.cles):
			chaine+="{} : {}, ".format(cle,self.valeurs[index])		
		chaine=chaine[:len(chaine)-2] #supprime la derniere virgule		
		chaine+='}'
		return chaine
	
	def __iter__(self):
		"""iterateur de la classe qui permet de la parcourir"""
		for index,cle in enumerate(self.cles):
			yield (cle,self.valeurs[index])
		

	#def __next__(self):
	#"""implementation de la fonction permettant le parcours de la classe"""

	def __str__(self):
		"""permet d'afficher la classe avec print de facon plus jolie"""
		

	def __getitem__(self,cle):
		"""methode executee lorsqu'on tape objet[cle]"""
		try:
			i=self.cles.index(cle)
			return self.valeurs[i]
		except ValueError:
			print("The key \"{}\" does not exist".format(cle))
			return None

	def __setitem__(self,cle,valeur):
		"""methode executee lorsqu'on tape objet[cle] = valeur"""
		try:
			i=self.cles.index(cle)
			self.valeurs[i]=valeur
		except ValueError:
			self.cles.append(cle)
			self.valeurs.append(valeur)

	def __contains__(self,cle):
		"""methode qui permet d'utiliser le mot-cle 'in'. Renvoie 'True' ou 'False'"""
	
	def __len__(self):
		"""methode qui permet de connaitre la taille de l'objet"""

	def __additem__(self,dico):
		"""methode permettant de faire objet1 + objet2"""

jean=DictionnaireOrdonne()
gabriel=DictionnaireOrdonne({1:'jea'})
vince=DictionnaireOrdonne(jean = 5,gabriel=1,FX=5)
