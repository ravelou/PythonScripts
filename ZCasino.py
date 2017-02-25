#!/usr/bin/python3.5
from random import randrange
from math import ceil

def lancerRoulette():
	numeroTire=randrange(50)
	return numeroTire

def deMemeCouleur(numRoulette, numJoueur):
	pariteNumRoulette=numRoulette%2
	pariteNumJoueur=numJoueur%2

	if pariteNumJoueur == pariteNumRoulette:
		return True
	else:
		return False

def Gain(numRoulette,numJoueur,mise):
	if numRoulette == numJoueur:
		print("Bravo, vous avez tire le bon numero : ", numRoulette, "\nVous remportez ",mise*3,"$")
		return mise+mise*3

	elif deMemeCouleur(numRoulette,numJoueur):
		print("Les chiffres sont de meme parite, vous remportez ",ceil(mise*0.5)," $")
		return mise+ceil(0.5*mise)
	else:
		print("Perdu, vous perdez votre mise de ",mise,"$")
		return 0 

portemonnaie=100
print("vous possedez ",portemonnaie, "$")

while portemonnaie > 0:
	mise=int(input("Combien voulez-vous miser ?"))
	portemonnaie-=mise
	numeroParie=int(input("Quel est le nombre sur lequel vous pariez ?"))
	numeroTire=lancerRoulette()
	print("Le numero tire est le ",numeroTire)
	portemonnaie+=Gain(numeroTire,numeroParie,mise)
	print("Vous possedez ",portemonnaie," $ dans votre portemonnaie")

 

