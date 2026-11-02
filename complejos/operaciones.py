"""
operaciones.py
----------------------------------------------------
Operaciones con números complejos.

Autor: Proyecto Calculadora de Números Complejos
"""

import cmath
import math

from complejos.conversiones import redondear
from .parser import convertir


# =====================================================
# Operaciones básicas
# =====================================================

def suma(z1: complex, z2: complex):
    return complex(round((z1 + z2).real,2),round((z1 + z2).imag,2))


def resta(z1: complex, z2: complex) -> complex:
    return complex(round((z1 - z2).real,2),round((z1 - z2).imag,2))


def multiplicacion(z1: complex, z2: complex) -> complex:
    return complex(round((z1 * z2).real,2),round((z1 * z2).imag,2))


def division(z1: complex, z2: complex) -> complex:
    if z2 == 0:
        raise ZeroDivisionError("No es posible dividir entre cero.")
    return complex(round((z1 / z2).real,2),round((z1 / z2).imag,2))


# =====================================================
# Operaciones individuales
# =====================================================

def conjugado(z: complex) -> complex:
    return  complex(round((z.conjugate()).real,2),round((z.conjugate()).imag,2))

# =====================================================
# Potencias
# =====================================================

def potencia(z: complex, n: int) -> complex:
    """
    Calcula z^n
    """
    return complex(round((z ** n).real,2),round((z ** n).imag,2))


# =====================================================
# Raíces n-ésimas
# =====================================================

def raices(z: complex, n: int) -> complex:
    """
    Devuelve todas las raíces n-ésimas.

    Resultado:
        lista de números complejos
    """

    r = abs(z)
    theta = cmath.phase(z)

    modulo_raiz = r ** (1 / n.real)

    resultado = []

    for k in range(int(n.real)):

        angulo = (theta + 2 * math.pi * k) / n.real

        raiz = complex(
            modulo_raiz * math.cos(angulo),
            modulo_raiz * math.sin(angulo)
        )

        resultado.append(
            complex(round(raiz.real, 2), round(raiz.imag, 2))
        )

    return resultado

# =====================================================
# Pruebas
# =====================================================

if __name__ == "__main__":

    z1 = complex(3, 4)
    z2 = complex(2, -1)

    print("Suma:", suma(z1, z2))
    print("Resta:", resta(z1, z2))
    print("Multiplicación:", multiplicacion(z1, z2))
    print("División:", division(z1, z2))
    print("Potencia:", potencia(z1, 3))
    print("Raíces cúbicas:")

    for r in raices(z1, 3):
        print(r)
