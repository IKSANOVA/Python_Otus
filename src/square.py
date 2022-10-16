# from Python_Otus.src.figure import Figure
from .figure import Figure

class Square(Figure):
    def __init__(self, a):
        pi = 3.14
        super(Square, self).__init__('Square')
        self._set_p(pi * a * a)
        self._set_s(a*a)

    
    