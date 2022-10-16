from figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    def triangle (self):
        print(f'a = {self.a}')
        print(f'b = {self.b}')
        print(f'c = {self.c}')
        print(f'S = {self.s}')
        print(f'P = {self.p}')