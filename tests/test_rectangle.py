from src import Rectangle

def test_rectangle_positive():
    a = Rectangle(10, 20)
    b = Rectangle(20, 10)    
    area = a.add_area(b)
    assert a.s == b.s
    assert a.p == b.p
    assert area == (10*10) + (20*20)
    print(area)


def test_rectangle_negative():
    error = None
    try:
        a = Rectangle(10, 20)
        area = a.add_area(10)
        print(area)
    except ValueError as ex:
        error = ex
    assert error is not None        
