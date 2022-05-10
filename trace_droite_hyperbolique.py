import math
import matplotlib.pyplot as plt



def norme(vecteur):
    """
    Prend un couple de coordonnées représentant un vecteur en deux dimensions et revoie sa norme
    """
    return math.sqrt(vecteur[0] ** 2 + vecteur[1] ** 2)



def intersection_geodesique_abscisse(pointA, pointB, precision=0.01):
    """
    Prend deux couples de coordonnées en entrée et renvoie un tuple (centre[0], R), avec centre[0] l'abscisse du centre du cercle et R son rayon. Attention, ce programme est conçu pour des points dans le demi-plan de Poincaré !
    """
    if int(pointA[0] * 1000) == int(pointB[0] * 1000):  # pour deux points de même abscisse : droite d'équation x = pointA[0]
        return (pointA[0], 0)   # rayon nul par convention
    
    milieu_segment = ((pointA[0] + pointB[0]) / 2, (pointA[1] + pointB[1]) / 2)
    
    if pointB[0] - pointA[0] < 0:
        pointA, pointB = pointB, pointA
        
    vect_radial = ((pointB[1] - pointA[1]), -(pointB[0] - pointA[0]))
    centre = [milieu_segment[0], milieu_segment[1]]     #list() ne fonctionne plus ??!
    
    assert vect_radial[1] < 0
    
    norme_vect = norme(vect_radial)
    vect_unitaire_radial = (vect_radial[0] / norme_vect, vect_radial[1] / norme_vect)
    
    while centre[1] > 0:
        centre[0] += vect_unitaire_radial[0] * precision
        centre[1] += vect_unitaire_radial[1] * precision
        
    rayon = math.sqrt((pointA[0] - centre[0]) ** 2 + pointA[1] ** 2)
    
    return (centre[0], rayon)
    
    

def points_cercle(abscisse_centre, rayon, nombre_points=100):
    """
    Renvoie deux listes contenant les coordonnees selon x et y des points d'un demi-cercle de rayon donné 
    et de centre situé sur l'axe des abscisses d'abscisse donnée
    """
    liste_abscisses = [abscisse_centre - rayon + i * (2 * rayon) / nombre_points for i in range(nombre_points)] + [abscisse_centre + rayon]
    liste_ordonnees = [math.sqrt(abs(rayon ** 2 - (x - abscisse_centre) ** 2)) for x in liste_abscisses] 
    return liste_abscisses, liste_ordonnees


def points_segment(
    abscisse_centre, rayon, pointA, pointB, nombre_points=10000, precision=0.001
):
    """
    Renvoie deux listes contenant les coordonnees selon x et y des points d'une portion de cercle de centre et de
    rayon donnés, entre les points pointA et pointB
    """
    liste_abscisses = [
        abscisse_centre - rayon + i * (2 * rayon) / nombre_points
        for i in range(nombre_points)
    ] + [abscisse_centre + rayon]
    liste_ordonnees = [
        math.sqrt(abs(rayon**2 - (x - abscisse_centre) ** 2)) for x in liste_abscisses
    ]
    liste_abscisses_finale = []
    liste_ordonnees_finale = []
    for i in range(len(liste_abscisses)):
        if (
            liste_abscisses[i] - precision <= pointA[0]
            and pointB[0] <= liste_abscisses[i] + precision
        ) or (
            liste_abscisses[i] - precision <= pointB[0]
            and pointA[0] <= liste_abscisses[i] + precision
        ):
            liste_abscisses_finale.append(liste_abscisses[i])
            liste_ordonnees_finale.append(liste_ordonnees[i])
    return liste_abscisses_finale, liste_ordonnees_finale


def trace_droite(A, B):
    """
    Trace la droite hyperbolique passant par les points A et B, avec A et B des tuples
    """    
    if A[0] == B[0]:
        plt.plot([A[0], B[0]], [A[1], B[1]])
    cercle = intersection_geodesique_abscisse(A, B)

    points_du_cercle = points_cercle(cercle[0], cercle[1])
    abscisses = points_du_cercle[0]
    ordonnees = points_du_cercle[1]
    plt.plot(abscisses, ordonnees)
    plt.plot(abscisses, [0 for i in abscisses], c="black")


def trace_segment(A, B):
    """
    Trace le segment hyperbolique entre les points A et B, avec A et B des tuples
    """
    if A[0] == B[0]:
        plt.plot([A[0], B[0]], [A[1], B[1]])
    cercle = intersection_geodesique_abscisse(A, B)

    points_du_cercle = points_segment(cercle[0], cercle[1], A, B)
    abscisses = points_du_cercle[0]
    ordonnees = points_du_cercle[1]
    plt.plot(abscisses, ordonnees)
    plt.plot(abscisses, [0 for i in abscisses], c="black")


def trace_segment_noir(A, B):
    """
    Trace un segment hyperbolique noir entre les points A et B, avec A et B des tuples
    """
    if A[0] == B[0]:
        plt.plot([A[0], B[0]], [A[1], B[1]], c="black")
    cercle = intersection_geodesique_abscisse(A, B)

    points_du_cercle = points_segment(cercle[0], cercle[1], A, B)
    abscisses = points_du_cercle[0]
    ordonnees = points_du_cercle[1]
    plt.plot(abscisses, ordonnees, c="black")
    plt.plot(abscisses, [0 for i in abscisses], c="black")
    
    
    """
A = (2, 1)
B = (1, 2)
cercle = intersection_geodesique_abscisse(A, B)
print(cercle)


points_du_cercle = points_cercle(cercle[0], cercle[1])
abscisses = points_du_cercle[0]
ordonnees = points_du_cercle[1]

plt.scatter([A[0], B[0], cercle[0]], [A[1], B[1], 0], c = "red")


plt.plot(abscisses, ordonnees)
plt.plot(abscisses, [0 for i in abscisses], c = "black")

plt.axis("equal")
plt.title("Tracé de la droite hyperbolique reliant deux points")
    
plt.show()

"""




