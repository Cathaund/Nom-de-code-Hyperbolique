import numpy as np
import itertools
import matplotlib.pyplot as plt
from trace_mediatrice import trace_la_mediatrice
from trace_droite_hyperbolique import trace_segment_noir

A = np.matrix("4 0; 0 1")
B = np.matrix("5 3; 3 5")
C = np.linalg.inv(A)
D = np.linalg.inv(B)

liste_combinaisons = list(itertools.product("ABCD", repeat=3))
liste_matrices = []
partie_reelle = []
partie_imaginaire = []

for combinaison in liste_combinaisons:
    liste_pour_cette_combinaison = []
    for lettre in combinaison:
        if lettre == "A":
            liste_pour_cette_combinaison.append(A)
        if lettre == "B":
            liste_pour_cette_combinaison.append(B)
        if lettre == "C":
            liste_pour_cette_combinaison.append(C)
        if lettre == "D":
            liste_pour_cette_combinaison.append(D)
    liste_matrices.append(liste_pour_cette_combinaison)

liste_points_pour_tracer = []
for combinaison in liste_matrices:
    liste_intermediaire = []
    for i in range(len(combinaison)):
        P = np.matrix("1 0; 0 1")
        for index_point in combinaison[:i]:
            P = P * index_point
        Z = np.matrix("1 0; 0 1")
        Z = P * Z
        point_associe = (Z[0, 0] * 1j + Z[0, 1]) / (Z[1, 0] * 1j + Z[1, 1])
        point_associe = (point_associe.real, point_associe.imag)
        liste_intermediaire.append(point_associe)
    liste_points_pour_tracer.append(liste_intermediaire)

for i in range(len(liste_points_pour_tracer)):
    print(i)
    for index_point in range(len(liste_points_pour_tracer[i]) - 1):
        trace_la_mediatrice(
            liste_points_pour_tracer[i][index_point],
            liste_points_pour_tracer[i][index_point + 1],
        )
        trace_segment_noir(
            liste_points_pour_tracer[i][index_point],
            liste_points_pour_tracer[i][index_point + 1],
        )
        partie_reelle.append(liste_points_pour_tracer[i][index_point][0])
        partie_imaginaire.append(liste_points_pour_tracer[i][index_point][1])
    partie_reelle.append(liste_points_pour_tracer[i][-1][0])
    partie_imaginaire.append(liste_points_pour_tracer[i][-1][1])

# plt.scatter(partie_reelle, partie_imaginaire)
plt.axis("equal")
plt.show()
