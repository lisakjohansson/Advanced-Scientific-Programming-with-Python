import pytest
import simple_math

def test_simple_add():
    assert simple_math.simple_add(2, 3) == 5
    assert simple_math.simple_add(-1, 1) == 0

def test_simple_sub():
    assert simple_math.simple_sub(5, 3) == 2
    assert simple_math.simple_sub(0, 4) == -4

def test_simple_mult():
    assert simple_math.simple_mult(3, 4) == 12
    assert simple_math.simple_mult(-2, 3) == -6

def test_simple_div():
    assert simple_math.simple_div(10, 2) == 5
    assert simple_math.simple_div(3, 2) == 1.5

def test_simple_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        simple_math.simple_div(1, 0)

def test_poly_first():
    # a0 + a1*x
    assert simple_math.poly_first(2, 1, 3) == 7   # 1 + 3*2
    assert simple_math.poly_first(0, 5, 10) == 5

def test_poly_second():
    # a0 + a1*x + a2*x^2
    assert simple_math.poly_second(2, 1, 3, 4) == 23  # 1 + 3*2 + 4*4
    assert simple_math.poly_second(0, 5, 10, 20) == 5