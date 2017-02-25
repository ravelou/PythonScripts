#!/usr/bin/python3.5
# -*-coding:utf-8 -* 
annee=int(input("Taper une année : "))
#yprint(type(annee))

if annee%4==0:
	if annee%100==0:
		if annee%400==0:
			print(annee, "est une annee bissextile")
		else:
			print(annee,  "n\'est pas une annee bissextile")
	else:
		print(annee, "est une annee bissextile")
else:
	print(annee, "n\'est pas une annee bissextile")
	
