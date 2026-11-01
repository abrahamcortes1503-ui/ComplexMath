"""
graficas.py
---------------------------------------------------------
Funciones para graficar números complejos utilizando Plotly.

Autor: Proyecto Calculadora de Números Complejos
"""

import plotly.graph_objects as go


# ======================================================
# Calcular límites automáticos
# ======================================================

def calcular_limites(*numeros):
    """
    Ajusta automáticamente los límites del plano
    para que todos los números sean visibles.
    """

    reales = [z.real for z in numeros if z is not None]
    imaginarios = [z.imag for z in numeros if z is not None]

    if not reales:
        return -5, 5, -5, 5

    xmin = min(reales)
    xmax = max(reales)

    ymin = min(imaginarios)
    ymax = max(imaginarios)

    margen = max(
        xmax - xmin,
        ymax - ymin,
        2
    ) * 0.30

    return (
        xmin - margen,
        xmax + margen,
        ymin - margen,
        ymax + margen
    )


# ======================================================
# Agregar un vector
# ======================================================

def agregar_vector(fig, z, nombre, color):

    fig.add_trace(

        go.Scatter(

            x=[0, z.real],
            y=[0, z.imag],

            mode="lines+markers+text",

            text=["", nombre],

            textposition="top center",

            name=nombre,

            line=dict(
                color=color,
                width=3
            ),

            marker=dict(
                size=10,
                color=color
            )
        )
    )


# ======================================================
# Agregar punto
# ======================================================

def agregar_punto(fig, z, nombre, color):

    fig.add_trace(

        go.Scatter(

            x=[z.real],
            y=[z.imag],

            mode="markers+text",

            text=[nombre],

            textposition="top center",

            marker=dict(

                size=12,

                color=color

            ),

            name=nombre

        )

    )


# ======================================================
# Graficar dos números y resultado
# ======================================================

def graficar(z1, z2=None, resultado=None):

    fig = go.Figure()

    if z1 is not None:
        agregar_vector(fig, z1, "Z₁", "blue")

    if z2 is not None:
        agregar_vector(fig, z2, "Z₂", "green")

    if resultado is not None:
        agregar_vector(fig, resultado, "Resultado", "red")

    xmin, xmax, ymin, ymax = calcular_limites(
        z1,
        z2,
        resultado
    )

    fig.update_xaxes(

        range=[xmin, xmax],

        zeroline=True,

        zerolinewidth=2,

        zerolinecolor="black",

        gridcolor="lightgray"

    )

    fig.update_yaxes(

        range=[ymin, ymax],

        zeroline=True,

        zerolinewidth=2,

        zerolinecolor="black",

        gridcolor="lightgray",

        scaleanchor="x",

        scaleratio=1

    )

    fig.update_layout(

        title="Plano Complejo",

        xaxis_title="Parte Real",

        yaxis_title="Parte Imaginaria",

        template="plotly_white",

        width=700,

        height=700,

        legend=dict(

            orientation="h",

            y=1.05

        )

    )

    return fig


# ======================================================
# Paralelogramo de la suma
# ======================================================

def graficar_suma(z1, z2, resultado):

    fig = go.Figure()

    agregar_vector(fig, z1, "Z₁", "blue")
    agregar_vector(fig, z2, "Z₂", "green")
    agregar_vector(fig, resultado, "Z₁ + Z₂", "red")

    # Lados del paralelogramo

    fig.add_trace(

        go.Scatter(

            x=[z1.real, resultado.real],

            y=[z1.imag, resultado.imag],

            mode="lines",

            line=dict(

                dash="dash",

                color="gray"

            ),

            showlegend=False

        )

    )

    fig.add_trace(

        go.Scatter(

            x=[z2.real, resultado.real],

            y=[z2.imag, resultado.imag],

            mode="lines",

            line=dict(

                dash="dash",

                color="gray"

            ),

            showlegend=False

        )

    )

    xmin, xmax, ymin, ymax = calcular_limites(
        z1,
        z2,
        resultado
    )

    fig.update_xaxes(range=[xmin, xmax])
    fig.update_yaxes(
        range=[ymin, ymax],
        scaleanchor="x",
        scaleratio=1
    )

    fig.update_layout(

        title="Suma mediante la Regla del Paralelogramo",

        template="plotly_white",

        width=700,

        height=700

    )

    return fig


# ======================================================
# Gráfica de raíces
# ======================================================

def graficar_raices(z,raices):
        fig = go.Figure()

        # =====================================================
        # Número original
        # =====================================================

        fig.add_trace(
            go.Scatter(
                x=[0, z.real],
                y=[0, z.imag],
                mode="lines+markers",
                name="z",
                line=dict(width=3),
                marker=dict(size=10)
            )
        )

        # =====================================================
        # Raíces
        # =====================================================

        for i, raiz in enumerate(raices):
            nombre = f"Raíz {i + 1}"

            fig.add_trace(

                go.Scatter(

                    x=[0, raiz.real],

                    y=[0, raiz.imag],

                    mode="lines+markers+text",

                    name=nombre,

                    text=[
                        "",
                        nombre
                    ],

                    textposition="top center",

                    marker=dict(
                        size=9
                    )

                )

            )

        # =====================================================
        # Plano
        # =====================================================

        fig.update_layout(

            title="Raíces enésimas de un número complejo",

            xaxis_title="Parte real",

            yaxis_title="Parte imaginaria",
            template="plotly_white",

            xaxis=dict(
                zeroline=True,
                zerolinewidth=2
            ),

            yaxis=dict(
                zeroline=True,
                zerolinewidth=2,
                scaleanchor="x",
                scaleratio=1
            ),

            height=650

        )

        fig.update_xaxes(

            zeroline=True,

            zerolinewidth=2,

            zerolinecolor="black",

            gridcolor="lightgray"

        )

        fig.update_yaxes(

            zeroline=True,

            zerolinewidth=2,

            zerolinecolor="black",

            gridcolor="lightgray",

            scaleanchor="x",

            scaleratio=1

        )

        return fig


# ======================================================
# Pruebas
# ======================================================

if __name__ == "__main__":

    z1 = complex(3, 4)

    z2 = complex(1, -2)

    r = z1 + z2

    fig = graficar(z1, z2, r)

    fig.show()