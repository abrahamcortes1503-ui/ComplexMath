#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 11:13:34 2025

@author: abrahamcortes

--------------------------------------------
Convierte números complejos escritos en
distintas formas a un objeto complex de Python.

Formatos soportados:

3+4i
3+4j
5-2i
7
-4i

5<30
5∠30
5∠30°

5 cis 30
5 CIS 30

5exp(i30)
5e^(i30)
5e^(i30°)
"""

import re
import cmath
import math


def convertir(texto):
    """
    Convierte diferentes representaciones de un número complejo
    a un objeto complex de Python.
    """

    if texto is None:
        raise ValueError(
            "No se recibió ningún valor."
        )

    texto = str(texto).strip()

    texto = texto.replace(" ", "")

    texto = texto.replace("I", "i")

    texto = texto.replace("j", "i")

    # Eliminar paréntesis externos
    if texto.startswith("(") and texto.endswith(")"):
        texto = texto[1:-1]

    # ==================================================
    # FORMA EXPONENCIAL
    #
    # 5e^(iπ/3)
    # 5e^(i60°)
    # ==================================================

    patron_exp = (
        r"^([+-]?\d*\.?\d+)"
        r"e\^\(i(.+)\)$"
    )

    coincidencia = re.match(
        patron_exp,
        texto
    )

    if coincidencia:
        modulo = float(
            coincidencia.group(1)
        )

        angulo = math.radians(
            coincidencia.group(2)
        )

        return cmath.rect(
            modulo,
            angulo
        )

    # ==================================================
    # FORMA POLAR
    #
    # 5∠60°
    # 5∠π/3
    # ==================================================

    patron_polar = (
        r"^([+-]?\d*\.?\d+)"
        r"cis"
        r"([+-]?\d*\.?\d+)"
        r"°?$"
    )

    coincidencia = re.match(
        patron_polar,
        texto
    )

    if coincidencia:
        modulo = float(
            coincidencia.group(1)
        )

        angulo = math.radians(float(
            coincidencia.group(2)
        ))
        #print(modulo)
        #print(angulo)
        return cmath.rect(
            modulo,
            angulo
        )

    # ==================================================
    # FORMA BINÓMICA
    # ==================================================

    if "i" in texto:

        texto_python = texto.replace(
            "i",
            "j"
        )

        try:

            return complex(
                texto_python
            )

        except ValueError:

            pass

    # ==================================================
    # NÚMERO REAL
    # ==================================================

    try:

        return complex(
            float(texto),
            0
        )

    except ValueError:

        raise ValueError(
            f"Formato no reconocido: {texto}"
        )



