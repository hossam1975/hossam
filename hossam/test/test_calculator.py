import pytest
from src import calculator as calc
day=26   
test_data = [(2, 3,-1), (-1, -1, -2), (0, 0, 0) , (10, 5, 5), (100, 200, -100)]

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

@pytest.mark.parametrize("input1,input2,result", test_data)                                                  
def test_subtract(input1, input2, result):
    assert calc.subtract(input1, input2) == result
    
@pytest.mark.skip       
def test_multiply():
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(0, 100) == 0   
@pytest.mark.january    
def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 0) == "Error: division by zero"
    assert calc.divide(-6, -2) == 3
def test_return_null():
    assert calc.return_null() is None   
def test_power():
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(-2, 2) == 4
def test_modulus():
    assert calc.modulus(10, 3) == 1
    assert calc.modulus(5, 5) == 0
    assert calc.modulus(-7, 4) == 1
def test_floor_divide():
    assert calc.floor_divide(10, 3) == 3
    assert calc.floor_divide(5, 0) == "Error: division by zero"
    assert calc.floor_divide(-7, 2) == -4
def test_square_root():
    assert calc.square_root(16) == 4
    assert calc.square_root(-4) == "Error: negative input"
    assert calc.square_root(0) == 0
def test_cube_root():
    assert calc.cube_root(27) == 3
    assert calc.cube_root(-8) == -2
    assert calc.cube_root(0) == 0
@pytest.mark.skipif(day<28, reason="Bill payment tests run only on the 28th or later of the month")   
def test_bill_payment():
    print   ("This is a placeholder test for bill payment functionality.")