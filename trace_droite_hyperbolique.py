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
    Renvoie deux listes contenant les coordonnees selon x et y des points d'un cercle de centre et de rayon donnés
    """
    liste_abscisses = [abscisse_centre - rayon + i * (2 * rayon) / nombre_points for i in range(nombre_points)] + [abscisse_centre + rayon]
    liste_ordonnees = [math.sqrt(abs(rayon ** 2 - (x - abscisse_centre) ** 2)) for x in liste_abscisses] 
    return liste_abscisses, liste_ordonnees
    
    
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




