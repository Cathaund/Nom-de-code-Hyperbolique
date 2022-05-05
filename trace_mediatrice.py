# encoding utf-8
""" L'objectif de ce programme est de tracer la médiatrice à un segment en géométrie hyperbolique.
DONNÉES EN ENTRÉE :
    * deux couple de coordonnées des points A et B dans le demi-plan de Poincaré

RÉSULTAT :
    * un couple (c, R), avec c la position du centre du cercle sur l'axe des abscisses et R le rayon du cercle, qui sont ensuite traités avec la bibliothèque Matplotlib pour tracer la droite hyperbolique correspondante
    
ÉTAPES SUCCESSIVES :
    * on trouve le milieu M du segment AB à l'aide de la formule du birapport
    * on calcule l'équation de la tangente à la courbe à l'aide de l'équation du demi-cercle (dont on connaît le rayon et la position du centre grâce au programme de tracé de droite hyperbolique)
    * on calcule la position c du point d'intersection entre la tangente à la droite hyperbolique en M et l'axe des abscisses
    * on trace le cercle de centre c et de rayon dist(c, M)
    
Bonne lecture !
"""
import math
import matplotlib.pyplot as plt

import trace_droite_hyperbolique

def eucli(A, B):
    """
    renvoie la distance euclidienne entre deux points exprimés en couples de coordonnées (tuple ou liste)
    """
    return math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)


def birapport(pointA, pointB):
    """
    prend deux couples de coordonnées pointA et pointB en entrée et renvoie la distance hyperbolique entre pointA et pointB
    """
    if pointA[0] > pointB[0]:
        pointA, pointB = pointB, pointA
    droite_AB = trace_droite_hyperbolique.intersection_geodesique_abscisse(pointA, pointB, precision = 0.001)
    #  pointA_inf correspond à l'intersection à gauche avec l'axe des abscisses ; on part du centre et on retranche le rayon
    pointA_inf = (droite_AB[0] - droite_AB[1], 0)
    pointB_inf = (droite_AB[0] + droite_AB[1], 0)
    birapport_calc = (eucli(pointB, pointA_inf) * eucli(pointA, pointB_inf)) / (eucli(pointA, pointA_inf) * eucli(pointB, pointB_inf))
    return abs(math.log(birapport_calc))


def milieu_AB(pointA, pointB):
    """
    prend deux points pointA et pointB en entrée, récupère les coordonnées des points 
    sur la portion de droite hyperbolique entre pointA et pointB et y fait évoluer un point M 
    jusqu'à ce que birapport(pointA, M) ~= birapport(pointB, M)
    """
    if pointA[0] > pointB[0]:
        pointA, pointB = pointB, pointA

    coord_droite_hyp = trace_droite_hyperbolique.intersection_geodesique_abscisse(pointA, pointB)

    liste_coordonnees = trace_droite_hyperbolique.points_cercle(coord_droite_hyp[0], coord_droite_hyp[1])
    liste_abscisses = liste_coordonnees[0]
    liste_ordonnees = liste_coordonnees[1]
    pointM = (liste_abscisses[1], liste_ordonnees[1])
    increment = 1
    while pointM[0] < pointA[0] or birapport(pointA, pointM) < birapport(pointB, pointM):
        pointM = (liste_abscisses[increment], liste_ordonnees[increment])
        increment += 1

    return pointM


def equation_cercle(x, abscisse_centre, rayon):
    """
    prend une abscisse et renvoie l'ordonnée d'un point du cercle
    """
    return math.sqrt(rayon ** 2 - (x - abscisse_centre) ** 2)


def coef_directeur_tangente_cercle(x, abscisse_centre, rayon):
    """
    prend une abscisse d'un point du cercle et renvoie le coefficient directeur de la tangente à la courbe
    """
    print("rayon au carré moins x -c au carré : ", rayon ** 2 - (x - abscisse_centre) ** 2)
    return (abscisse_centre - x) / math.sqrt(rayon ** 2 - (x - abscisse_centre) ** 2)


def intersection_tangenteM_abscisses(pointA, pointB):
    """
    prend en entrée les coordonnées de deux points pointA et pointB, et calcule l'intersection 
    entre l'axe des abscisses et la tangente à la courbe au milieu pointM du segment hyperbolique [AB]
    renvoie ensuite la position du point d'intersection ainsi que la distance entre pointM et ce point

    abscisse_centre = trace_droite_hyperbolique.intersection_geodesique_abscisse(pointA, pointB, precision = 0.01)[0]
    rayon = trace_droite_hyperbolique.intersection_geodesique_abscisse(pointA, pointB, precision = 0.01)[1]
    la tangente au point M(x_m, y_m) d'un cercle a pour équation y'(x_m) * (x - x_m) + y_m, 
    avec y'(x_m) = coef_directeur_tangente_cercle(x_m, abscisse_centre, rayon)
    On résout alors y'(x_m) * (x - x_m) + y_m = 0 ssi x = -y_m / y'(x_m) + x_m
    """
    abscisse_centre = trace_droite_hyperbolique.intersection_geodesique_abscisse(pointA, pointB, precision = 0.01)[0]
    rayon = trace_droite_hyperbolique.intersection_geodesique_abscisse(pointA, pointB, precision = 0.01)[1]

    print()
    print("Rayon calculé", rayon)
    print("Distance centre-A", eucli(pointA, (abscisse_centre, 0)))
    print()

    pointM = milieu_AB(pointA, pointB)

    print("Point M :", pointM)

    abscisse_intersection = (- pointM[1] / coef_directeur_tangente_cercle(pointM[0], abscisse_centre, rayon) + pointM[0])
    
    print(abscisse_intersection)

    return (abscisse_intersection, eucli(pointM, (abscisse_intersection, 0)))
    

def points_mediatrice(pointA, pointB, nombre_points=100):
    """
    prend en entrée les points pointA et pointB et renvoie deux listes contenant respectivement 
    les abscisses et les ordonnées des nombre_points du cercle (en subdivision régulière)
    """
    centre, rayon = intersection_tangenteM_abscisses(pointA, pointB)[0], intersection_tangenteM_abscisses(pointA, pointB)[1]
    
    liste_points = trace_droite_hyperbolique.points_cercle(centre, rayon, nombre_points)

    return liste_points





A = (2, 1)
B = (1, 2)
print(eucli(A, B))
print(eucli(B, A))
print(birapport(A, B))
print(birapport(B, A))

M = milieu_AB(A, B)
print(M)
print()

print()

print(coef_directeur_tangente_cercle(M[0], 0, eucli((0, 0), B)))

cercle = intersection_tangenteM_abscisses(A, B)
print(cercle)


abscisse_du_centre = trace_droite_hyperbolique.intersection_geodesique_abscisse(A, B)[0]
rayon = trace_droite_hyperbolique.intersection_geodesique_abscisse(A, B)[1]
points_cercle_ori = trace_droite_hyperbolique.points_cercle(abscisse_du_centre, rayon)
abscisses_ori = points_cercle_ori[0]
ordonnees_ori = points_cercle_ori[1]
plt.plot(abscisses_ori, ordonnees_ori, c = "green")

points_du_cercle = points_mediatrice(A, B)
abscisses = points_du_cercle[0]
ordonnees = points_du_cercle[1]

plt.scatter([A[0], B[0], cercle[0]], [A[1], B[1], 0], c = "red")


plt.plot(abscisses, ordonnees)
plt.plot(abscisses, [0 for i in abscisses], c = "black")

plt.axis("equal")
plt.title("Tracé de la médiatrice hyperbolique reliant deux points")
    
plt.show()
