from libreria_pytest import fibonacci, palindromo, factoria

def test_fibonacci_cinco():
    assert fibonacci(5) == 5

def test_palindromo_anita():
    assert palindromo("Anita lava la tina")

def test_factorial_cinco():
    assert factoria(5) == 120