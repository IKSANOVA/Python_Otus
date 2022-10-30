from src.triangle import Triangle

class TestTriangle:

    def test_area(self):
        triangle_a = Triangle(4, 3, 4)
        assert triangle_a.area == 5.562148865321747, 'Не верно считается площать треугольника'


    def test_perimeter(self):
        triangle_p = Triangle(4, 3, 4)
        assert triangle_p.perimeter == 11, 'Не верно считается периметр треугольника'
        