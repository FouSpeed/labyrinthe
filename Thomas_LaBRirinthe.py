#/bin/python

from os import O_CREAT
from matplotlib import pyplot as plt
import random, math, time, itertools
#import numpy as np
import math

import logging

#logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
arr = []
def changeValue(array, x, y, value):
	"""changer le nbr dans array de coordonnées [x,y] par la valeur "value"
		variables : 
			array: tableau d'entrée
			x: abscisse du point du tableau à modifier
			y: ordonnée du point du tableau à modifier
			value: valeur à intégrer au point du tableau à modifier
	"""
	array[x][y] = value

def next (x, y, rangeRow, rangeCol):    
	"""
	renvoie la case suivante en fonction de la position d'origine
	variables:
		x: abscisse du point d'origine  
		y: ordonnée du point d'origine
		rangeRow: nombre de lignes
		rangeCol: nombre de colonnes
	"""
	
	# initialise variables
	test = False
	xOriginalValue= x
	yOriginalValue = y
	#logging.info("original value x : " + str(xOriginalValue))
	#logging.info("original value y : " + str(yOriginalValue))	
	
	while test == False :
		direction = random.choice(["N", "S", "E", "W"])
		#logging.info("direction: " + str(direction))
		if direction == "N":
			y -= 1
		elif direction == "S":
			y += 1
		elif direction == 'E':
			x += 1
		else:
			x -= 1
		if x >= 0 and x <= rangeRow and  y>=0 and y <= rangeCol:
			test = True
			#logging.info("final value x : " + str(x))
			#logging.info("final value y : " + str(y))
		else:
			#revenir a l'ancienne valeure
			#logging.info('Destination not in the array. Try to find another point.')
			x = xOriginalValue
			y = yOriginalValue
			
	values = [x,y]
	return values

def bordLabyrinthe (array):
    #au bord du tableau les point sont égaux à 2 
	for x in range(len(array)):
		changeValue(array, x, 0, 2)
		changeValue(array, x, len(array[0])-1, 2)
	for y in range(len(array[1])):
		changeValue(array, 0, y, 2)
		changeValue(array, len(array)-1, y, 2)

def toucheBord(value):
    if value == 2:
        return True
    else:
        return False

def voisinBord(array):
    xBord = random.randint(0, len(array[0])-1)
    yBord = random.randint(0, len(array)-1)
    while xBord != 0 and xBord != len(array[0])-1 and yBord != 0 and yBord != len(array)-1:
        xBord = random.randint(0, len(array[0])-1)
        yBord = random.randint(0, len(array)-1)
    return [xBord, yBord]
"""
    if xBord == 0 or xBord == len(array[0])-1:
        yBord = random.randint(0, len(array)-1)
    else:
        yBord = random.choice([0, len(array)-1])
    return [xBord, yBord]
"""

def arreteBord(array):
	plt.plot([0 , len(array[0])-1], [0 , 0], color='Black', lw= 5)
	plt.plot([ 0, len(array[0])-1],[ len(array)-1 , len(array)-1], color='Black', lw= 5)
	plt.plot([0 , 0],[ 0 , len(array)-1], color='Black', lw= 5)
	plt.plot([len(array[0])-1 , len(array[0])-1], [0 , len(array)-1], color='Black', lw= 5)

def enterExit(array):
	xEnter = 0
	xExit = len(array[0])-1
	yEnter = random.randint(0, len(array)-2)
	yExit =  random.randint(0, len(array)-2)
	plt.plot([xEnter, xEnter],[yEnter, yEnter+1], color = "r", lw= 5)
	plt.plot([xExit, xExit],[yExit, yExit +1], color = "r", lw= 5)
		

"""
	enter = voisinBord(array)
	exit = voisinBord(array)
	while enter == exit:
		enter = voisinBord(array)
		exit = voisinBord(array)
	if enter[0] == 0:
		try:
			plt.plot([enter[0],enter[0]+1],[enter[1],enter[1]+1], color="Blue")
		except:
			plt.plot([enter[0],enter[0]-1],[enter[1],enter[1]-1], color="Blue")
		try:
			plt.plot([exit[0],exit[0]+1],[exit[1],exit[1]+1], color="Blue")
		except:
			plt.plot([exit[0],exit[0]-1],[enter[1],exit[1]-1], color="Blue")
"""		
#input
rows = int(input("How many row(s) : "))
cols = int(input("How many col(s) : "))

# Create array
arrString = 'arr = ' + "[" + ("[" + "0," * (cols -1) + "0" + "],") * (rows-1) +("[" + "0," * (cols -1) + "0" + "]") +"]"
exec(arrString)
	
# Identify random original point
oRow = random.randint(0, len(arr)-1)
oCol = random.randint(0, len(arr[0])-1)

while arr[oRow] == 0 or arr[oRow] == len(arr[0])-1 or arr[oCol] == 0 or arr[oCol] == len(arr)-1:
	logging.info(str(oRow) + "," + str(oCol) + " : Ca touche pas le bord , on cherche un nouveau point d'origine")
	oRow = random.randint(0, len(arr)-1)
	oCol = random.randint(0, len(arr[0])-1)
logging.info("point d'origine : " + str(oRow) + "," + str(oCol))
		
		
# Initialize number max of possible sommets and number remaining sommets
sommetMax = rows * cols 
sommetRemaining = rows * cols  #-1 pour le point d'origine
logging.info("Max de sommets pouvant être construits : " + str(sommetMax))	


#Construction de l'arbre

sommet = [oRow, oCol]
while sommetRemaining > 0:
	logging.info("sommets restants : " + str(sommetRemaining))
	nextSommet = next(sommet[0], sommet[1], rows-1, cols-1)
	logging.info("next sommet : " + str(nextSommet))
	valueNextSommet = int(arr[nextSommet[0]][nextSommet[1]])
	logging.info("valeur nouveau sommet : " + str(valueNextSommet))
	logging.info("original value of the next sommet: " + str(valueNextSommet))
	if valueNextSommet == 0:
		if nextSommet[0] == 0 or nextSommet[0] == len(arr[0])-1 or nextSommet[1] == 0 or nextSommet[1] == len(arr)-1:
			logging.info("Ca touche le bord")
			changeValue(arr, nextSommet[0], nextSommet[1], 1)
			sommetRemaining -= 1
			sommet = voisinBord(arr)
			logging.info("sommet : " + str(sommet))
			nextSommet = next(sommet[0], sommet[1], rows-1, cols-1)
			logging.info("next sommet2 : " + str(nextSommet))
		else:
			logging.info("value of next sommet is 0. It will be changed")
			changeValue(arr, nextSommet[0], nextSommet[1], 1)
			logging.info("l'arrête formée est: " + str(sommet) + " " + str(nextSommet))
			plt.plot([sommet[0] , nextSommet[0]], [sommet[1] , nextSommet[1]], color='k')
			sommetRemaining -= 1
			sommet = nextSommet
	elif valueNextSommet == 1:
		sommet = nextSommet

"""
for _ in arr:
	for i in _:
		print(i,end=" ")
	print()
"""

arreteBord(arr)
enterExit(arr)
plt.axis([0, rows-1, 0, cols-1])
plt.grid(False)
plt.show()
plt.close()
