from main import quadratic_multiply, BinaryNumber



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(20), BinaryNumber(20)) == 20*20
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert quadratic_multiply(BinaryNumber(15), BinaryNumber(15)) == 15*15
