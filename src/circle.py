from .figure import Figure

class Circle(Figure):
    def __init__(self, a):
        super(Circle, self).__init__('Circle')
        self._set_p(a*4)
        self._set_s(a*a)