import os
import random

from django.conf import settings
from django.http import JsonResponse

from django.shortcuts import render

from .conversiones import polar, redondear
from .graficas import graficar, graficar_raices
from .parser import convertir
from .operaciones import (
    suma,
    resta,
    multiplicacion,
    division,
    potencia,
    conjugado,
    raices
)


def imagen_aleatoria(request):

    carpeta = os.path.join(
        settings.BASE_DIR,
        "static",
        "images"
    )

    extensiones_validas = (
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp"
    )

    imagenes = [
        archivo
        for archivo in os.listdir(carpeta)
        if archivo.lower().endswith(
            extensiones_validas
        )
    ]

    if not imagenes:

        return JsonResponse(
            {
                "error": "No hay imágenes disponibles."
            },
            status=404
        )

    imagen = random.choice(
        imagenes
    )

    return JsonResponse(
        {
            "url": f"/static/images/{imagen}"
        }
    )

def inicio(request):
    resultado = None
    grafica_html = None
    error = None

    if request.method == "POST":

        numero1 = request.POST.get(
            "numero1"
        )

        numero2 = request.POST.get(
            "numero2"
        )

        operacion = request.POST.get(
            "operacion"
        )

        try:

            # Convertimos el primer número
            z1 = convertir(
                numero1
            )

            z2 = convertir(
                numero2
            )

            # ==========================================
            # Seleccionar operación
            # ==========================================

            if operacion == "suma":

                resultado = suma(
                    z1,
                    z2
                )

                grafica = graficar(
                    z1,
                    z2,
                    resultado

                )

                grafica_html = grafica.to_html(

                    full_html=False,

                    include_plotlyjs="cdn"
                )





            elif operacion == "resta":

                resultado = resta(
                    z1,
                    z2
                )

                grafica = graficar(
                    z1,
                    z2,
                    resultado

                )

                grafica_html = grafica.to_html(

                    full_html=False,

                    include_plotlyjs="cdn"
                )

            elif operacion == "multiplicacion":

                resultado = multiplicacion(
                    z1,
                    z2
                )

                grafica = graficar(
                    z1,
                    z2,
                    resultado

                )

                grafica_html = grafica.to_html(

                    full_html=False,

                    include_plotlyjs="cdn"
                )

            elif operacion == "division":

                resultado = division(
                    z1,
                    z2
                )

                grafica = graficar(
                    z1,
                    z2,
                    resultado

                )

                grafica_html = grafica.to_html(

                    full_html=False,

                    include_plotlyjs="cdn"
                )

            elif operacion == "conjugado":

                if z2 is None:
                    numero = z1
                else:
                    numero = z2

                    # Calcular el conjugado
                resultado = conjugado(numero)

                grafica = graficar(numero, None, resultado)

                grafica_html = grafica.to_html(

                    full_html=False,

                     include_plotlyjs="cdn"
                )



            elif operacion == "potencia":

                resultado = potencia(
                    z1,
                    z2
                )

                grafica = graficar(
                    z1,
                    z2,
                    resultado

                )

                grafica_html = grafica.to_html(

                    full_html=False,

                    include_plotlyjs="cdn"
                )

            elif operacion == "raiz":

                resultado = raices(
                    z1,
                    z2
                )

                for i in resultado:
                    print(i)

                grafica = graficar_raices(
                    z1, resultado
                )

                grafica_html = grafica.to_html(

                    full_html=False,

                    include_plotlyjs="cdn"
                )

            else:

                error = "Selecciona una operación."

        except ValueError as e:

            error = str(e)

        except ZeroDivisionError as e:

            error = str(e)





    return render(

        request,

        "complejos/index.html",

        {

            "resultado": resultado,
            "grafica_html": grafica_html

        }

    )
