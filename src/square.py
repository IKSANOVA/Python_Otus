# from Python_Otus.src.figure import Figure
from .figure import Figure

class Square(Figure):
    def __init__(self, a):
        super(Square, self).__init__('Square')
        self._set_p(a*4)
        self._set_s(a*a)

    
    