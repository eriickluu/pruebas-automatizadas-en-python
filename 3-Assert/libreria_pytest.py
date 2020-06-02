# -Pytest se puede generar pruebas unitarias con instalar la libreria 
# -La librería pytest se utilizara siempre y cuando las pruebas sean sencillas

def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number - 1) + fibonacci(number -2)

def palindromo(sentence):
   sentence = str(sentence).lower().replace(" ", "")
   return sentence == sentence[::-1]

def factoria(number):
    if number == 0: return 1
    else: return number * factoria(number -1)