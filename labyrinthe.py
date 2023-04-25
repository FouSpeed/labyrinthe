from matplotlib import pyplot as plt
import random
#import numpy as np
import math

from pyparsing import col

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

    while test == False :
        direction = random.choice(["N", "S", "E", "W"])
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
        else:
            x = xOriginalValue
            y = yOriginalValue
            
    values = [x,y]
    return values

def voisinBord(rows, cols):
    # renvoie les coordonnées d'un nouveau point touchant le bord du labyrinthe
    # rows : nombre de lignes du labyrinthe
    # cols : nombre de colonnes du labyrinthe
    xBord = random.randint(0, cols-1)
    yBord = random.randint(0, rows-1)
    while xBord != 0 and xBord != rows-1 and yBord != 0 and yBord != cols-1:
        xBord = random.randint(0, cols-1)
        yBord = random.randint(0, rows-1)
    return [xBord, yBord]


def arreteBord(rows, cols):
    # crée les arrêtes autour du labyrinthe
    # rows : nombre de lignes du labyrinthe
    # cols : nombre de colonnes du labyrinthe
    plt.plot([0 , rows-1], [0,0], color='k', lw= 5) # Sud
    plt.plot([rows-1,rows-1],[0,cols-1],color='k', lw= 5) # Est
    plt.plot([0,0],[ 0 , cols-1], color='k', lw= 5) # ouest
    plt.plot([0,rows-1], [cols-1,cols-1], color='k', lw= 5) # Nord


def _enter(cols):
    # renvoie les coordonnées l'entrée du labyrinthe
    # rows : nombre de lignes du labyrinthe
    xEnter = 0
    yEnter = random.randint(0, cols-2)
    plt.plot([xEnter, xEnter],[yEnter, yEnter+1], color = "w", lw= 5)
    return [xEnter, yEnter]
    
def _exit(rows, cols):
    # renvoie les coordonnées la sortie du labyrinthe
    # rows : nombre de lignes du labyrinthe
    # cols : nombre de colonnes du labyrinthe
    xExit = rows-1
    yExit =  random.randint(0, cols-2)
    plt.plot([xExit, xExit],[yExit, yExit +1], color = "w", lw= 5)
    return [xExit, yExit]   

def labyrinthe(rows, cols):
    # crée un labyrinthe, et retourne l'ensemble des arrêtes du  labyrinthe, les coordonnées de la case de départ, les coordonnées de la case de sortie
    # rows : nombre de lignes du labyrinthe
    # cols: nombre de colonnes du labyrinthe

    arr = [[0 for i in range (cols)] for j in range(rows)]

    # Identify random original point
    oRow = random.randint(0, rows-1)
    oCol = random.randint(0, cols-1)
    while oRow != 0 and oRow != rows-1 and oCol != 0 and oCol != cols-1:
        oRow = random.randint(0, rows-1)
        oCol = random.randint(0, cols-1)
            
    # Initialize number max of possible sommets, number of remaining sommets and list of arretes
    sommetRemaining = rows * cols  #-1 pour le point d'origine
    arrete = []

    #Construction de l'arbre
    sommet = [oRow, oCol]
    while sommetRemaining > 0:
        nextSommet = next(sommet[0], sommet[1], rows-1, cols-1)
        valueNextSommet = int(arr[nextSommet[0]][nextSommet[1]])
        if valueNextSommet == 0:
            if nextSommet[0] == 0 or nextSommet[0] == cols-1 or nextSommet[1] == 0 or nextSommet[1] == rows-1:
                changeValue(arr, nextSommet[0], nextSommet[1], 1)
                sommetRemaining -= 1
                sommet = voisinBord(rows, cols)
                nextSommet = next(sommet[0], sommet[1], rows-1, cols-1)
            else:
                changeValue(arr, nextSommet[0], nextSommet[1], 1)
                plt.plot([sommet[0] , nextSommet[0]], [sommet[1] , nextSommet[1]], color='k')
                arrete += [[[sommet[0] , sommet[1]], [nextSommet[0] , nextSommet[1]]]]
                sommetRemaining -= 1
                sommet = nextSommet
        elif valueNextSommet == 1:
            sommet = nextSommet
    arreteBord(rows, cols)
    enter = _enter(cols)
    exit = _exit(rows, cols)
    return [arrete, enter, exit]


def initialisationDistance(cols, rows):
    # initialise une valeur max sur l'ensemble des cases du labyrinthe
    # cols = abscisse
    # rows = ordonnées
    valeurs = [[cols*rows*10 for i in range(cols)]for j in range(rows)]
    return valeurs

def rv(arrete):
    return [arrete[1],arrete[0]]

def possibleWay(arrete , position, row, col):
    # renvoie l'ensemble des sorties possible d'une case
    # arrete : liste des arrêtes du labyrinthe
    # position : coordonnées [x,y] de la position actuelle
    # row : nombre de lignes du labyrinthe
    # col : nombre de colonnes du labyrinthe
    voisin = []
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
    # donne la valeur à chaque case du labyrinthe correspondant à la distance parcourue pour y accéder.
    # enter : coordonnées de la case de départ
    # arrete : liste de toutes les arrêtes du labyrinthe
    # row : nombre de lignes du labyrinthe
    # col : nombre de colonnes du labyrinthe
    valeurs = [[col*row*10 for i in range(col)]for j in range(row)]
    retour = [[[-1,-1] for i in range(col)]for j in range(row)]
    retour[enter[1]][enter[0]]= enter
    liste = [[enter, 0, enter]]
    valeurs[enter[1]][enter[0]] = 0
    while liste != []: # la liste est vide quand on a fait toutes les cases
        l2 = []
        for l in liste:
            for v in possibleWay(arrete, l[0], row, col):
                if valeurs[v[1]][v[0]] > l[1]+1:
                    valeurs[v[1]][v[0]] = l[1]+1
                    l2.append([v, l[1]+1, l[0]])
                    retour[v[1]][v[0]] = l[0]
                    #plt.text(v[0]+0.5,v[1]+0.5,str(l[1]+1))
        liste = l2
    return [valeurs, retour]
        
def chemin(exit, retour):
    # renvoie la liste des coordonnées des cases à utiliser pour aller de l'entrée à la sortie du labyrinthe 
    # exit : coordonnées de la case de sortie
    # retour : liste des cordonnées pour revenir au point de départ
    point = [exit[0]-1, exit[1]]
    chemin = [point]
    while True : 
        X = retour[point[1]][point[0]]
        if X != point:
            point = X
            chemin.append(X)
        else:
            return chemin

def plotChemin (Chemin):
    # dessine un chemin
    # chemin : liste des coordonnées des différents points à relier
    for i in range (len(Chemin)-1):
        Z = Chemin[i]
        Zp = Chemin[i+1]
        plt.plot([Z[0]+0.5, Zp[0]+0.5],[Z[1]+0.5, Zp[1]+0.5], color = "r", lw = 3)