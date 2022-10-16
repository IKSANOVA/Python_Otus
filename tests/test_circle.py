from src import Circle

def test_circle_positive():
    pi = 3.14
    a = Circle(10)
    b = Circle(20)    
    area = a.add_area(b)
    assert area == (pi * a * a)
    print(area)


def test_circle_negative():
    error = None
    try:
        a = Circle(10)
        area = a.add_area(10)
        print(area)
    except ValueError as ex:
        error = ex
    assert error is not None        
