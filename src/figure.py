class Figure:
    def __init__(self, name):
        self.name = name
        self.s = 0
        self.p = 0
        
    def _set_s(self, s):
        self.s = s
        
    def _set_p(self, p):
        self.p = p
        
    def add_area(self, b):
        if not isinstance(b, Figure):
            raise ValueError()
        return self.s + b.s

    def __str__(self):
        return(f'Class = {self.__class__.__name__}, Name = {self.name}, S = {self.s}, P = {self.p}')


# if __name__ == '__main__':
#     f = Figure('base')
#     print(f)