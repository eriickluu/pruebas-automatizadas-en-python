"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120
"""

class Recursivo:
    def factoria(self, number):
        if number == 0: return 1
        else: return number * self.factoria(number -1)
