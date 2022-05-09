import numpy as np
import itertools
import matplotlib.pyplot as plt
from TraceDisque import trace_segment_disque, trace_disque


def du_plan_au_disque(Z):
    matrice = np.matrix("1j 1; 1 1j")
    return matrice * Z


trace_disque()

A = np.matrix("4 0; 0 1")
B = np.matrix("5 3; 3 5")
C = np.linalg.inv(A)
D = np.linalg.inv(B)

liste_combinaisons = list(itertools.product("ABCD", repeat=4))
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
    for lettre in range(len(combinaison)):
        P = np.matrix("1 0; 0 1")
        for index_point in combinaison[:lettre]:
            P = P * index_point
        Z = np.matrix("1 0; 0 1")
        Z = du_plan_au_disque(P * Z)
        point_associe = (Z[0, 0] * 1j + Z[0, 1]) / (Z[1, 0] * 1j + Z[1, 1])
        liste_intermediaire.append(point_associe)
    liste_points_pour_tracer.append(liste_intermediaire)

for lettre in range(len(liste_points_pour_tracer)):
    for index_point in range(len(liste_points_pour_tracer[lettre]) - 1):
        trace_segment_disque(
            liste_points_pour_tracer[lettre][index_point],
            liste_points_pour_tracer[lettre][index_point + 1],
        )
        partie_reelle.append(liste_points_pour_tracer[lettre][index_point].real)
        partie_imaginaire.append(liste_points_pour_tracer[lettre][index_point].imag)
    partie_reelle.append(liste_points_pour_tracer[lettre][-1].real)
    partie_imaginaire.append(liste_points_pour_tracer[lettre][-1].imag)

#plt.scatter(partie_reelle, partie_imaginaire)
plt.axis("equal")
plt.show()
