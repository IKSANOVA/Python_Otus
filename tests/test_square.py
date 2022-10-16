from src import Square

def test_square_positive():
    a = Square(10)
    b = Square(20)    
    area = a.add_area(b)
    assert area == (10*10) + (20*20)
    print(area)


def test_square_negative():
    error = None
    try:
        a = Square(10)
        area = a.add_area(10)
        print(area)
    except ValueError as ex:
        error = ex
    assert error is not None        
