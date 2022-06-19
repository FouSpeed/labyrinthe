#/bin/python

# import libraries
from matplotlib import pyplot as plt
from fonction import *

# get inputs
while True:
    try :
        taille = int(input("taille du labyrinthe : "))
        break
    except:
        print ("Vous devez entrer un nombre")

X = Y = taille

# initialize labyrinthe
arr = labyrinthe(X,Y)

# Donne une valeur aux cases du labyrinthe, correspondant à la distance parcourue pour y accéder
initialisationDistance(X,Y)
valueRetour = changeValueDistance(arr[1], arr[0], X-1, Y-1)

# retrouve le chemin le plus court etl e dessine
retour = valueRetour[1]
path = chemin(arr[2], retour)
plotChemin(path)

# affiche le résultat
plt.show()
