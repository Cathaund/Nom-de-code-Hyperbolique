import math
import matplotlib.pyplot as plt


def points_cercle_disque(abscisse_centre, ordonnee_centre, rayon, nombre_points=10000):
    """
    Renvoie deux listes contenant les coordonnees selon x et y des points d'un cercle de centre et de
    rayon donnés 
    """
    liste_abscisses = [
        abscisse_centre - rayon + i * (2 * rayon) / nombre_points
        for i in range(nombre_points)
    ] + [abscisse_centre + rayon]
    liste_ordonnees = [
        math.sqrt(abs(rayon**2 - (x - abscisse_centre) ** 2)) + ordonnee_centre
        for x in liste_abscisses
    ]
    liste_ordonnees2 = [
        -math.sqrt(abs(rayon**2 - (x - abscisse_centre) ** 2)) + ordonnee_centre
        for x in liste_abscisses
    ]
    liste_ordonnees2.reverse()
    liste_ordonnees.extend(liste_ordonnees2)
    liste_abscisses2 = [
        abscisse_centre - rayon + i * (2 * rayon) / nombre_points
        for i in range(nombre_points)
    ] + [abscisse_centre + rayon]
    liste_abscisses2.reverse()
    liste_abscisses.extend(liste_abscisses2)
    return liste_abscisses, liste_ordonnees


def points_segment_disque(
    abscisse_centre, ordonnee_centre, rayon, zA, zB, nombre_points=10000
):
    """
    Renvoie deux listes contenant les coordonnees selon x et y des points d'un cercle de centre et de
    rayon donnés
    """
    liste_abscisses = [
        abscisse_centre - rayon + i * (2 * rayon) / nombre_points
        for i in range(nombre_points)
    ] + [abscisse_centre + rayon]
    liste_ordonnees = [
        math.sqrt(abs(rayon**2 - (x - abscisse_centre) ** 2)) + ordonnee_centre
        for x in liste_abscisses
    ]
    liste_ordonnees2 = [
        -math.sqrt(abs(rayon**2 - (x - abscisse_centre) ** 2)) + ordonnee_centre
        for x in liste_abscisses
    ]
    liste_ordonnees2.reverse()
    liste_ordonnees.extend(liste_ordonnees2)
    liste_abscisses2 = [
        abscisse_centre - rayon + i * (2 * rayon) / nombre_points
        for i in range(nombre_points)
    ] + [abscisse_centre + rayon]
    liste_abscisses2.reverse()
    liste_abscisses.extend(liste_abscisses2)

    liste_abscisses_finale = []
    liste_ordonnees_finale = []

    for i in range(len(liste_ordonnees)):
        if (
            (liste_ordonnees[i] > zA.imag and zB.imag > liste_ordonnees[i])
            or (liste_ordonnees[i] > zB.imag and zA.imag > liste_ordonnees[i])
        ) and (
            (liste_abscisses[i] < zA.real and zB.real < liste_abscisses[i])
            or (liste_abscisses[i] < zB.real and zA.real < liste_abscisses[i])
        ):
            liste_abscisses_finale.append(liste_abscisses[i])
            liste_ordonnees_finale.append(liste_ordonnees[i])
    return liste_abscisses_finale, liste_ordonnees_finale

"""
Les deux prochaines fonctions ne sont pas de nous
"""

def determinant(zA, zB, precision=1e-12):
    """
    renvoie le déterminant des points zA et zB avec une précision donnée
    """
    d = zA.real * zB.imag - zA.imag * zB.real
    if abs(d) < precision:
        return 0
    else:
        return d


def hyperbolic_circle(zA, zB, precision=1e-15): 
    """
    retourne le centre et le rayon de la géodésique passant par deux points sur le disque de Poincaré
    """
    if (zA.real >= zB.real - precision and zA.real <= zB.real + precision) or (
        zA.imag >= zB.imag - precision and zA.imag <= zB.imag + precision
    ):
        return (False, zA, zB)
    else:
        a = (zA.imag * (1 + abs(zB) ** 2) - zB.imag * (1 + abs(zA) ** 2)) / determinant(
            zA, zB
        )
        b = (zB.real * (1 + abs(zA) ** 2) - zA.real * (abs(zB) ** 2 + 1)) / determinant(
            zA, zB
        )
        zI = -a / 2 - b / 2 * 1j
        r = math.sqrt(abs(a**2 / 4 + b**2 / 4 - 1))
        return True, zI, r


def trace_disque():
    """
    trace le disque de rayon unité
    """
    liste_abscisses, liste_ordonnees = points_cercle_disque(0, 0, 1)
    plt.plot(liste_abscisses, liste_ordonnees, c="black")


def trace_geodesique_disque(zA, zB):
    """
    trace la géodésique entre deux nombres imaginaires zA et zB donnés
    """
    plt.scatter([zA.real, zB.real], [zA.imag, zB.imag])
    if hyperbolic_circle(zA, zB)[0]:
        a, z_centre, rayon = hyperbolic_circle(zA, zB)
        liste_abscisses_point, liste_ordonnees_point = points_cercle_disque(
            z_centre.real, z_centre.imag, rayon
        )
        plt.plot(liste_abscisses_point, liste_ordonnees_point)
    else:
        plt.plot([zA.real, zB.real], [zA.imag, zB.imag])


def trace_segment_disque(zA, zB):
    """
    trace le segment entre deux nombres imaginaires zA et zB donnés
    """
    if hyperbolic_circle(zA, zB)[0]:
        a, z_centre, rayon = hyperbolic_circle(zA, zB)
        liste_abscisses_point, liste_ordonnees_point = points_segment_disque(
            z_centre.real, z_centre.imag, rayon, zA, zB
        )
        plt.plot(liste_abscisses_point, liste_ordonnees_point)
    else:
        plt.plot([zA.real, zB.real], [zA.imag, zB.imag])


"""a = 0.5 + 0.4j
b = -0.5 + 0.2j
trace_disque()
trace_geodesique_disque(a, b)
axes = plt.gca()
plt.axis("equal")
plt.plot()
plt.show()"""
