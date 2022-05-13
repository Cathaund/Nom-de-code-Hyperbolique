import numpy as np
import itertools
import matplotlib.pyplot as plt
from trace_droite_hyperbolique import trace_segment

A = np.matrix("4 0; 0 1")
B = np.matrix("5 3; 3 5")
C = np.linalg.inv(A)
D = np.linalg.inv(B)

LONGUEUR_MOT = 4

c1 = (1.53, 1.30)
c2 = (-1.50, 1.30)
c3 = (-0.37, 0.33)
c4 = (0.37, 0.33)

liste_combinaisons = []
for i in range(LONGUEUR_MOT):
    liste_combi = list(itertools.product("ABCD", repeat = i + 1))
    liste_combinaisons.extend(liste_combi)


print(liste_combinaisons)

"""
On construit une liste (liste_mot) contenant les mots de matrice de la longeur chosie
"""
liste_mots = []

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


liste_points_domaines = [[c1, c2, c3, c4]]
for mot in liste_mots:
    for lettre in range(len(mot)):
        liste_points_image = []
        P = np.matrix("1 0; 0 1")
        for matrice in mot[:lettre]:
            P = P * matrice
        for point in liste_points_domaines[0]:
            image = (P[0, 0] * (point[0] + point[1] * 1j) + P[0, 1]) / (P[1, 0] * (point[0] + point[1] * 1j) + P[1, 1])
            liste_points_image.append((image.real, image.imag))
        print("Application de la matrice : ", liste_points_image)
        print()

    liste_points_domaines.append(liste_points_image)

print()
#print(liste_points_domaines)
print()

for i in liste_points_domaines:
    for j in range(3):
        trace_segment(i[j], i[j+1])
    trace_segment(i[-1], i[0])

#print(liste_points_domaines)



plt.axis("equal")
plt.show()