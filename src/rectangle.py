from .figure import Figure

class Rectangle(Figure):
    def __init__(self, h, l):
        super(Rectangle, self).__init__('Rectangle')
        self._set_p((h+l)*2)
        self._set_s(h*l)