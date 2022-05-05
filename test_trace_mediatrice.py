from trace_mediatrice import equation_cercle, coef_directeur_tangente_cercle, birapport, milieu_AB, intersection_tangenteM_abscisses, points_mediatrice


######___equation_cercle___######


def test_equation_cercle1():
    """
    test
    """
    x = 0
    rayon = 1
    assert equation_cercle(x, 0, rayon) > 0.9 and equation_cercle(x, 0, rayon) < 1.1


def test_equation_cercle2():
    """
    test2
    """
    x = 1
    rayon = 1
    assert abs(equation_cercle(x, 0, rayon)) < 0.1


def test_equation_cercle3():
    """
    test3
    """
    x = 0
    rayon = 1
    assert abs(equation_cercle(x, 1, rayon)) < 0.1


def test_equation_cercle4():
    """
    test4
    """
    x = 1
    rayon = 2
    assert equation_cercle(x, 1, rayon) > 1.9 and equation_cercle(x, 1, rayon) < 2.1


def test_equation_cercle5():
    """
    test5
    """
    x = 3
    rayon = 2.4
    assert equation_cercle(x, 2, rayon) > 2.1 and equation_cercle(x, 2, rayon) < 2.2


######___coef_directeur_tangente___######


def test_coef_directeur_tangente1():
    """
    test
    """
    x = 0
    rayon = 1
    assert abs(coef_directeur_tangente_cercle(x, 0, rayon)) < 0.1


def test_coef_directeur_tangente2():
    """
    test2
    """
    x = 0.99
    rayon = 1
    assert abs(coef_directeur_tangente_cercle(x, 0, rayon)) > 7


def test_coef_directeur_tangente3():
    """
    test3
    """
    x = 0.01
    rayon = 1
    assert abs(coef_directeur_tangente_cercle(x, 1, rayon)) > 7


def test_coef_directeur_tangente4():
    """
    test4
    """
    x = 1
    rayon = 2
    assert abs(coef_directeur_tangente_cercle(x, 1, rayon)) < 0.01


def test_coef_directeur_tangente5():
    """
    test5
    """
    x = 3
    rayon = 2.4
    assert coef_directeur_tangente_cercle(x, 2, rayon) < - 0.45 and coef_directeur_tangente_cercle(x, 2, rayon) > - 0.47



######___birapport()___######


def test_birapport1():
    """
    test1
    """
    pointA = (-0.5, 0.866)
    pointB = (0.5, 0.866)
    assert birapport(pointA, pointB) < birapport(pointB, pointA) + 0.1
   

def test_birapport2():
    """
    test2
    """
    pointA = (-0.5, 0.866)
    pointB = (0.5, 0.866)
    assert birapport(pointA, pointB) > birapport(pointB, pointA) - 0.1


def test_birapport3():
    """
    test3
    """
    pointA = (-0.5, 0.866)
    pointB = (0.5, 0.866)
    assert birapport(pointA, pointB) > 1.09
    

def test_birapport4():
    """
    test4
    """
    pointA = (-0.5, 0.866)
    pointB = (0.5, 0.866)
    assert birapport(pointA, pointB) < 2


def test_birapport5():
    """
    test5
    """
    pointA = (-0.81, 0.58)
    pointB = (0.31, 0.95)
    assert birapport(pointA, pointB) > 1.4


def test_birapport6():
    """
    test6
    """
    pointA = (-0.81, 0.58)
    pointB = (0.31, 0.95)
    assert birapport(pointA, pointB) < 1.5



######___milieu_AB___######


def test_milieu_AB1():
    """
    test1
    """
    pointA = (-0.8, 0.6)
    pointB = (0, 1)
    assert milieu_AB(pointA, pointB)[0] < milieu_AB(pointB, pointA)[0] + 0.1
    assert milieu_AB(pointA, pointB)[0] > milieu_AB(pointB, pointA)[0] - 0.1


def test_milieu_AB2():
    """
    test2
    """
    pointA = (-0.8, 0.6)
    pointB = (0, 1)
    assert milieu_AB(pointA, pointB)[1] < milieu_AB(pointB, pointA)[1] + 0.1
    assert milieu_AB(pointA, pointB)[1] > milieu_AB(pointB, pointA)[1] - 0.1


def test_milieu_AB3():
    """
    test3
    """
    pointA = (-0.8, 0.6)
    pointB = (0, 1)
    assert milieu_AB(pointA, pointB)[0] > - 0.55
    assert milieu_AB(pointA, pointB)[0] < -0.45


def test_milieu_AB4():
    """
    test4
    """
    pointA = (-0.8, 0.6)
    pointB = (0, 1)
    assert milieu_AB(pointA, pointB)[1] > 0.86
    assert milieu_AB(pointA, pointB)[1] < 0.88


def test_milieu_AB5():
    """
    test5
    """
    pointA = (0.61, 1.03)
    pointB = (0, 1.2)
    assert milieu_AB(pointA, pointB)[0] < milieu_AB(pointB, pointA)[0] + 0.1
    assert milieu_AB(pointA, pointB)[0] > milieu_AB(pointB, pointA)[0] - 0.1


def test_milieu_AB6():
    """
    test6
    """
    pointA = (0.61, 1.03)
    pointB = (0, 1.2)
    assert milieu_AB(pointA, pointB)[1] < milieu_AB(pointB, pointA)[1] + 0.1
    assert milieu_AB(pointA, pointB)[1] > milieu_AB(pointB, pointA)[1] - 0.1


def test_milieu_AB7():
    """
    test7
    """
    pointA = (0.61, 1.03)
    pointB = (0, 1.2)
    assert milieu_AB(pointA, pointB)[0] > 0.32
    assert milieu_AB(pointA, pointB)[0] < 0.34


def test_milieu_AB8():
    """
    test8
    """
    pointA = (0.61, 1.03)
    pointB = (0, 1.2)
    assert milieu_AB(pointA, pointB)[1] > 1.14
    assert milieu_AB(pointA, pointB)[1] < 1.16


def test_milieu_AB9():
    """
    test9
    """
    pointA = (0.5, 0.866)
    pointB = (0, 1)
    assert milieu_AB(pointA, pointB)[0] > 0.26
    assert milieu_AB(pointA, pointB)[0] < 0.28
    

def test_milieu_AB10():
    """
    test10
    """
    pointA = (0.5, 0.866)
    pointB = (0, 1)
    assert milieu_AB(pointA, pointB)[1] > 0.96
    assert milieu_AB(pointA, pointB)[1] < 0.98



######___intersection_tangenteM_abscisses()___######


def test_intersection_tangenteM_abscisses1():
    """
    test1
    """
    pointA = (0, 1)
    pointB = (0.5, 0.866)
    assert intersection_tangenteM_abscisses(pointA, pointB)[0] > 3


def test_intersection_tangenteM_abscisses2():
    """
    test2
    """
    pointA = (0, 1)
    pointB = (0.5, 0.866)
    assert intersection_tangenteM_abscisses(pointA, pointB)[1] > 3.1



######___points_mediatrice()___######


def test_points_mediatrice1():
    """
    test1
    """
    pointA = (0, 1)
    pointB = (0.5, 0.866)
    assert len(points_mediatrice(pointA, pointB)) == 2


def test_points_mediatrice2():
    """
    test2
    """
    pointA = (0, 1)
    pointB = (0.5, 0.866)
    assert len(points_mediatrice(pointA, pointB)[0]) == 101
    assert len(points_mediatrice(pointA, pointB)[1]) == 101


def test_points_mediatrice3():
    """
    test3
    """
    pointA = (0, 1)
    pointB = (0.5, 0.866)
    assert points_mediatrice(pointA, pointB)[0][0] > 0
    assert points_mediatrice(pointA, pointB)[0][0] < 0.5


def test_points_mediatrice4():
    """
    test4
    """
    pointA = (0, 1)
    pointB = (0.5, 0.866)
    assert points_mediatrice(pointA, pointB)[1][0] > - 0.1
    assert points_mediatrice(pointA, pointB)[1][0] <  0.1
