from src.rectangle import Rectangle

class TestRectangle:

    def test_area(self):
        rectangle_a = Rectangle(5, 7)
        assert rectangle_a.area == 35, 'Не верно считается площать прямоугольника'


    def test_perimeter(self):
        rectangle_p = Rectangle(5, 7)
        assert rectangle_p.perimeter == 24, 'Не верно считается периметр прямоугольника'