"""
conversiones.py
-----------------------------------------
Funciones para convertir números complejos
entre sus diferentes representaciones.

Autor: Proyecto Calculadora de Complejos
"""

import math


# ======================================================
# Redondeo bonito
# ======================================================

def redondear(valor: float, decimales: int = 4):
    """
    Evita mostrar números como
    3.00000000001
    """

    if abs(valor) < 1e-12:
        valor = 0

    return round(valor, decimales)


# ======================================================
# Forma binómica
# ======================================================

def binomica(z: complex, decimales: int = 4) -> str:
    """
    Devuelve:

    3 + 4i
    2 - 7i
    """

    a = redondear(z.real, decimales)
    b = redondear(z.imag, decimales)

    signo = "+" if b >= 0 else "-"

    return f"{a} {signo} {abs(b)}i"


# ======================================================
# Forma polar
# ======================================================

def polar(z: complex, decimales: int = 4):
    """
    Regresa:

    (r, theta)
    """

    r = redondear(abs(z), decimales)

    theta = redondear(
        math.degrees(
            math.atan2(z.imag, z.real)
        ),
        decimales
    )

    return r, theta


def polar_texto(z: complex, decimales: int = 4):

    r, ang = polar(z, decimales)

    return f"{r} ∠ {ang}°"


# ======================================================
# Forma exponencial
# ======================================================

def exponencial(z: complex, decimales: int = 4):

    r, ang = polar(z, decimales)

    return f"{r}e^(i{ang}°)"


# ======================================================
# Forma CIS
# ======================================================

def cis(z: complex, decimales: int = 4):

    r, ang = polar(z, decimales)

    return f"{r} cis {ang}°"


# ======================================================
# Conjugado
# ======================================================

def conjugado(z: complex):

    return z.conjugate()


# ======================================================
# Inverso
# ======================================================

def inverso(z: complex):

    if z == 0:
        return None

    return 1 / z


# ======================================================
# Norma
# ======================================================

def modulo(z: complex):

    return abs(z)


# ======================================================
# Argumento
# ======================================================

def argumento(z: complex):

    return math.degrees(
        math.atan2(
            z.imag,
            z.real
        )
    )


# ======================================================
# Información completa
# ======================================================

def informacion(z: complex):

    return {

        "real": redondear(z.real),

        "imaginaria": redondear(z.imag),

        "binomica": binomica(z),

        "polar": polar_texto(z),

        "exponencial": exponencial(z),

        "cis": cis(z),

        "modulo": redondear(modulo(z)),

        "argumento": redondear(argumento(z)),

        "conjugado": binomica(conjugado(z)),

        "inverso": (
            binomica(inverso(z))
            if inverso(z) is not None
            else "No existe"
        )

    }


# ======================================================
# Mostrar información
# ======================================================

def imprimir(z: complex):

    info = informacion(z)

    print("=" * 50)

    for clave, valor in info.items():
        print(f"{clave:15}: {valor}")

    print("=" * 50)


# ======================================================
# Prueba
# ======================================================

if __name__ == "__main__":

    z = complex(3, 4)

    imprimir(z)