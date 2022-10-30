from src.circle import Circle

class TestCircle:

    def test_area(self):
        circle_a = Circle(5)
        assert circle_a.area == 19.625, 'Не верно считается площать круга'

    def test_perimeter(self):
        circle_p = Circle(5)
        assert circle_p.perimeter == 15.700000000000001, 'Не верно считается периметр круга'