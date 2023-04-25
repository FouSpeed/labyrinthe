from labyrinthe import *


verification = False
while verification == False:
  X = int(input("donner un abscisse : "))
  Y = int(input("donner une ordoonée : "))
  solution = str(input("voulez-vous la solution (o/n)"))
  if X == Y:
    # initialize labyrinthe
    arr = labyrinthe(X,Y)
    if solution == "o":
        # Donne une valeur aux cases du labyrinthe, correspondant à la distance parcourue pour y accéder
        initialisationDistance(X,Y)
        valueRetour = changeValueDistance(arr[1], arr[0], X-1, Y-1)

        # retrouve le chemin le plus court et le dessine
        retour = valueRetour[1]
        path = chemin(arr[2], retour)
        plotChemin(path)

    # affiche le résultat
    plt.show()
    verification = True
  else:
    print("mettez des valeurs égales")
    verification = False