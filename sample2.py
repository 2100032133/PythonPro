import mathlib123

def test_cal_square_1():
    result = mathlib123.cal_square(5)
    assert result==25

def test_cal_square_2():
    result = mathlib123.cal_square(6)
    assert result== 36

def test_cal_square_4():
    result = mathlib123.cal_square(8)
    assert result == 64