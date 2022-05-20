import itertools
import matplotlib.pyplot as plt
import numpy as np

import trace_droite_hyperbolique
import trace_mediatrice


from trace_droite_hyperbolique import trace_segment


A = np.matrix("4 0; 0 1")
B = np.matrix("5 3; 3 5")
C = np.linalg.inv(A)
D = np.linalg.inv(B)

c1 = (1.53, 1.30)
c2 = (-1.50, 1.30)
c3 = (-0.37, 0.33)
c4 = (0.37, 0.33)

liste_points_domaines = [[c1, c2, c3, c4]]


Longueur_mot = 1

liste_combinaisons = list(itertools.product("ABCD", repeat=Longueur_mot + 1))
print(liste_combinaisons)
liste_mots = []

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
Pour chaque mot,  on crée une liste (liste_images) qui contient les coordonnées des images
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

        liste_points_domaines.append([])
        for point in liste_points_domaines[0]:
            imag = (P[0, 0] * (point[0] + point[1] * 1j) + P[0, 1]) / (P[1, 0] * (point[0] + point[1] * 1j) + P[1, 1])
            liste_points_domaines[-1].append((imag.real, imag.imag))

        coordonnées_image = (image.real, image.imag)
        liste_images.append(coordonnées_image)

        

    liste_points.append(liste_images)


"""
on relie maintenant les points contenus dans chaque liste de liste_point ensemble.
"""

for lettre in range(len(liste_points)):
    for index_point in range(len(liste_points[lettre]) - 1):
        trace_droite_hyperbolique.trace_segment(liste_points[lettre][index_point],
            liste_points[lettre][index_point + 1])
        

# relier c1 à c2 ; c2 à c3 ; c3 à c4 ; c4 à c1
for i in liste_points_domaines:
    for j in range(3):
        trace_droite_hyperbolique.trace_segment(i[j], i[j+1])
    trace_droite_hyperbolique.trace_segment(i[-1], i[0])

print(liste_points_domaines)


plt.axis("equal")
plt.show()
