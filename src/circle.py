from .figure import Figure

class Circle(Figure):
    def __init__(self, a):
        pi = 3.14
        super(Circle, self).__init__('Circle')
        self._set_p(pi * a * a)
        self._set_s(a*a)