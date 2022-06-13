#/bin/python

from os import O_CREAT
from matplotlib import pyplot as plt
import random, math, time, itertools
#import numpy as np
import math

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
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
	
#input
rows = int(input("How many row(s) : "))
cols = int(input("How many col(s) : "))

# Create array
arrString = 'arr = ' + "[" + ("[" + "0," * (cols -1) + "0" + "],") * (rows-1) +("[" + "0," * (cols -1) + "0" + "]") +"]"
exec(arrString)

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
	if xBord == 0 or xBord == len(array[0])-1:
		yBord = random.randint(0, len(array)-1)
	else:
		yBord = random.choice([0, len(array)-1])
	return [xBord, yBord]

	
# Identify random original point
oRow = random.randint(0, len(arr)-1)
oCol = random.randint(0, len(arr[0])-1)

bordLabyrinthe(arr)
while toucheBord(arr[oRow][oCol]) == False:
	if arr[oRow][oCol] != 2:
		oRow = random.randint(0, len(arr)-1)
		oCol = random.randint(0, len(arr[0])-1)
print(oRow , oCol)
		
		
# Initialize number max of possible sommets and number remaining sommets
sommetMax = rows * cols 
sommetRemaining = rows * cols  #-1 pour le point d'origine
logging.info("Max de sommets pouvant être construits : " + str(sommetMax))	
		
		


#Construction de l'arbre

sommet = [oRow, oCol]
while sommetRemaining > 0:
	print(sommetRemaining)
	nextSommet = next(sommet[0], sommet[1], rows-1, cols-1)
	logging.info("next sommet : " + str(nextSommet))
	valueNextSommet = int(arr[nextSommet[0]][nextSommet[1]])
	logging.info("original value of the next sommet: " + str(valueNextSommet))
	if valueNextSommet == 0:
		logging.info("value of next sommet is 0. It will be changed")
		changeValue(arr, nextSommet[0], nextSommet[1], 1)
		logging.info("l'arrête formée est: " + str(sommet) + " " + str(nextSommet))
		plt.plot([sommet[0] , nextSommet[0]], [sommet[1] , nextSommet[1]])
		sommetRemaining -= 1
		sommet = nextSommet
	if valueNextSommet == 1:
		sommet = nextSommet
	
	elif toucheBord(valueNextSommet):
	
		sommet = voisinBord(arr)
		logging.info("sommet : " + str(sommet))
		nextSommet = next(sommet[0], sommet[1], rows-1, cols-1)
		logging.info("next sommet2 : " + str(nextSommet))


		if toucheBord(arr[nextSommet[0]][nextSommet[1]]) == False:# and arr[nextSommet[0]][nextSommet[1]] == 0 :


			if arr[nextSommet[0]][nextSommet[1]] == 0:
				changeValue(arr, nextSommet[0], nextSommet[1], 1)
				logging.info("l'arrête formée est: " + str(sommet) + " " + str(nextSommet))
				plt.plot([sommet[0] , nextSommet[0]], [sommet[1] , nextSommet[1]])
				sommetRemaining -= 2
				sommet = nextSommet
			
			if arr[nextSommet[0]][nextSommet[1]] == 1:
				sommet = nextSommet


		elif toucheBord(arr[nextSommet[0]][nextSommet[1]]):
			sommet = voisinBord(arr)
	if sommetRemaining <= 14:
			plt.show()
			plt.close()
	#time.sleep(0.5)
		
		
		
		
		




for _ in arr:
	for i in _:
		print(i,end=" ")
	print()

plt.show()
plt.close()