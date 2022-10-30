from src.square import Square

class TestSquare:

    def test_area(self):
        square_a = Square(5)
        assert square_a.area == 25, 'Не верно считается площать круга'

    def test_perimeter(self):
        square_p = Square(5)
        assert square_p.perimeter == 20, 'Не верно считается периметр круга'