import numpy as np
import itertools
import matplotlib.pyplot as plt
from trace_droite_hyperbolique import trace_segment

A = np.matrix("4 0; 0 1")
B = np.matrix("5 3; 3 5")
C = np.linalg.inv(A)
D = np.linalg.inv(B)

Longueur_mot = 3

liste_combinaisons = list(itertools.product("ABCD", repeat=Longueur_mot + 1))
liste_mots = []
partie_reelle = []
partie_imaginaire = []

"""
On construit une liste (liste_mot) contenant les mots de matrice de la longeur chosie
"""

for mot in liste_combinaisons:
    mot_de_matrice = []
    for lettre in mot:
        if lettre == "A":
            mot_de_matrice.append(A)
        if lettre == "B":
            mot_de_matrice.append(B)
        if lettre == "C":
            mot_de_matrice.append(C)
        if lettre == "D":
            mot_de_matrice.append(D)
    liste_mots.append(mot_de_matrice)


"""
Pour chaque mot,  on crée une liste (liste_images) qui contient les coordonées des images
de z=i par les matrices composant le mot.
ex: (Pour le mot ABCD, liste_images contiendra les coordonnées de A(z), AB(z) , ABC(z) et ABCD(z)).
Puis on rajoute cette liste à liste_points
"""

liste_points = []
for mot in liste_mots:
    liste_images = []
    for lettre in range(len(mot)):
        P = np.matrix("1 0; 0 1")
        for index_point in mot[:lettre]:
            P = P * index_point
        image = (P[0, 0] * 1j + P[0, 1]) / (P[1, 0] * 1j + P[1, 1])
        coordonées_image = (image.real, image.imag)
        liste_images.append(coordonées_image)
    liste_points.append(liste_images)


"""
on relie maintenant les points contenus dans chaque liste de liste_point ensemble.
"""

for lettre in range(len(liste_points)):
    for index_point in range(len(liste_points[lettre]) - 1):
        trace_segment(
            liste_points[lettre][index_point],
            liste_points[lettre][index_point + 1],
        )
        partie_reelle.append(liste_points[lettre][index_point][0])
        partie_imaginaire.append(liste_points[lettre][index_point][1])
    partie_reelle.append(liste_points[lettre][-1][0])
    partie_imaginaire.append(liste_points[lettre][-1][1])

plt.axis("equal")
plt.show()
