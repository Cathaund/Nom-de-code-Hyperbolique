from trace_droite_hyperbolique import intersection_geodesique_abscisse


######___intersection_geodeisique_abscisse___######


def test_intersection_geodesique_abscisse1():
    """
    test1
    """
    pointA = (1, 0)
    pointB = (0, 1)
    assert intersection_geodesique_abscisse(pointA, pointB)[0] > -0.1
    assert intersection_geodesique_abscisse(pointA, pointB)[0] < 0.1


def test_intersection_geodesique_abscisse2():
    """
    test2
    """
    pointA = (1, 0)
    pointB = (0, 1)
    assert intersection_geodesique_abscisse(pointA, pointB)[1] > 0.9
    assert intersection_geodesique_abscisse(pointA, pointB)[1] < 1.1
    