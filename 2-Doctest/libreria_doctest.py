"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120
"""

def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number - 1) + fibonacci(number -2)

def palindromo(sentence):
    """Retorna verdadero si el parámetro es un palíndromo
    en caso sontrario retirna falso
   
    sentencia -- String o entero

    >>> palindromo("anita lava la tina")
    True
    """

   sentence = str(sentence).lower().replace(" ", "")
   return sentence == sentence[::-1]

class Recursivo:
    def factoria(self, number):
        if number == 0: return 1
        else: return number * self.factoria(number -1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile("test.txt")