import math
from collections import Counter

def media(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return 1

def mediana(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]

def moda(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    conteo = Counter(lista)
    max_frecuencia = max(conteo.values())
    modas = [k for k, v in conteo.items() if v == max_frecuencia]
    if len(modas) == len(lista):
        raise ValueError("No hay moda (todos los valores aparecen una vez)")
    return modas if len(modas) > 1 else modas[0]

def variance(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    m = media(lista)
    return sum((x - m) ** 2 for x in lista) / len(lista)

def ds(lista):
    return math.sqrt(variance(lista))

def coef_variacion(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    m = media(lista)
    if m == 0:
        raise ValueError("La media es cero, el coeficiente de variación no está definido")
    return (ds(lista) / m) * 100