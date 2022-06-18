#/bin/python
from matplotlib import pyplot as plt
import random, math, time, itertools
import numpy as np
import math
import sys
import logging

from fonction import labyrinthe
X = int(input("donner un abscisse : "))
Y = int(input("donner une ordoonée : "))


def initialisation (arr):
	L = []
	#toutes les parties du labyrinthe sont initialisés
	for row in range(len(arr)):
		for col in range(len(arr[row])):
			L  += [[[col, row], 0]]
	return L

def initialisationDistance(l, L):
	valeurs = [[l*L*10 for i in range(l)]for j in range(L)]
	return valeurs

def rv(arrete):
	return [arrete[1],arrete[0]]

def possibleWay(arrete , position, row, col):
	voisin = []
	# test des différentes directions
	# West:
	x, y = position[0], position[1]
	arreteEst = [[x+1, y], [x+1, y+1]]
	arreteWest = [[x, y],[ x, y+1]]
	arreteSouth = [[x, y], [x+1, y]]
	arreteNorth = [[x, y+1],[x+1, y+1]]
	if (arreteEst not in arrete) and (rv(arreteEst) not in arrete) and x< col -1:
		voisin.append([x+1, y])
	if (arreteWest not in arrete) and (rv(arreteWest) not in arrete) and x > 0:	
		voisin.append([x-1, y])
	if (arreteSouth not in arrete) and (rv(arreteSouth) not in arrete)and position[1] > 0 :	
		voisin.append([x, y-1])
	if (arreteNorth not in arrete ) and (rv(arreteNorth) not in arrete)and position[1] < row -1:	
		voisin.append([x, y+1])
	return voisin



def changeValueDistance(enter,arrete, row, col ):

	#print(possibleWay(arrete, [4,4], row-1, col-1))
	valeurs = [[col*row*10 for i in range(col)]for j in range(row)]
	#print(valeurs)
	retour = [[[-1,-1] for i in range(col)]for j in range(row)]
	retour[enter[1]][enter[0]]= enter
	liste = [[enter, 0, enter]]
	valeurs[enter[1]][enter[0]] = 0
	#profil = [1]
	while liste != []:
		l2 = []
		#print("liste = " + str(liste))
		for l in liste:
			#print("l[0] = " + str(l[0]) + " l = " + str(l))
			for v in possibleWay(arrete, l[0], row, col):
				#print("v = " + str(v))
				
				#print("v1 = " + str(v[1]))
				
				#print("v0 = " + str(v[0]))
				#print(valeurs[v[1]][v[0]])
				#print(l[1]+1)
				#print()	
				if valeurs[v[1]][v[0]] > l[1]+1:
					
					valeurs[v[1]][v[0]] = l[1]+1
					l2.append([v, l[1]+1, l[0]])
					retour[v[1]][v[0]] = l[0]
					#plt.text(v[0]+0.5,v[1]+0.5,str(l[1]+1))
					#print("valeurs = " + str(valeurs))
					#print("l2 = " + str(l2))
		#profil.append(len(l2))
		#print("profil = " + str(profil))
		liste = l2
		#print("list = " + str(list))
		
	return [valeurs, retour]
		
def chemin(exit, retour):
	#print("je commence")
	# correction piquet clôture
	point = [exit[0]-1, exit[1]]
	chemin = [point]
	#print("point = " + str(point))
	while True : 
		#print("a")
		#print("retour =" +  str(retour[point[1]][point[0]]))
		X = retour[point[1]][point[0]]
		if X != point:
			point = X
			chemin.append(X)
		else:
			#print("chemin = "+ str(chemin))
			return chemin

def plotChemin (Chemin):
	for i in range (len(Chemin)-1):
		Z = Chemin[i]
		Zp = Chemin[i+1]
		plt.plot([Z[0]+0.5, Zp[0]+0.5],[Z[1]+0.5, Zp[1]+0.5], color = "r", lw = 3)
		
		
		
arr = labyrinthe(X,Y)
#print(arr)


L = initialisation(arr[3])
#print(L)
initialisationDistance(X,Y)
valueRetour = changeValueDistance(arr[1], arr[0], X-1, Y-1)
#print(valueRetour)
retour = valueRetour[1]
#print(retour)
path = chemin(arr[2], retour)

plotChemin(path)


"""
for i in range(X-1):
	for j in range(Y-1):
		print(i, j, possibleWay(arr[0], [i, j], X-1, Y-1))
"""
plt.show()
plt.exit()
"""
				if valeurs[v[1]][v[0]] > l[1]+1 and firstValue != 0:
					
					valeurs[v[1]][v[0]] = l[1]+1
					l2.append([v, l[1]+1, l[0]])
				else:
					valeurs[v[1]][v[0]] = 0
					l2.append([enter, 0, enter])
"""

"""

"""
