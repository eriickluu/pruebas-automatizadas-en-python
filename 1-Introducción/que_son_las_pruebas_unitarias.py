def promedio(*args):
    return sum(args) / len(args)

def aprobatorio(promedio, minimo=70):
    return promedio >= minimo

def mensaje(aprobatorio=True):
    return "Felicidades" if aprobatorio else "Necesitas estudiar más."