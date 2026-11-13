const btnImagen =
    document.getElementById("btnImagen");

const modalImagen =
    document.getElementById("modalImagen");

const cerrarModal =
    document.getElementById("cerrarModal");

const contenedorImagen =
    document.getElementById("contenedorImagen");


btnImagen.addEventListener(
    "click",
    async function () {

        // Abrir ventana
        modalImagen.style.display = "flex";

        // Mensaje mientras carga
        contenedorImagen.innerHTML =
            "<p>Cargando imagen...</p>";

        try {

            const respuesta = await fetch(
                "/imagen-aleatoria/"
            );

            const datos =
                await respuesta.json();

            if (datos.url) {

                contenedorImagen.innerHTML = `
                    <img
                        src="${datos.url}"
                        alt="Imagen aleatoria"
                    >
                `;

            } else {

                contenedorImagen.innerHTML =
                    "<p>No se encontró ninguna imagen.</p>";
            }

        } catch (error) {

            console.error(error);

            contenedorImagen.innerHTML =
                "<p>Error al cargar la imagen.</p>";
        }

    }
);

cerrarModal.addEventListener(
    "click",
    function () {

        modalImagen.style.display = "none";

    }
);

window.addEventListener(
    "click",
    function (event) {

        if (event.target === modalImagen) {

            modalImagen.style.display = "none";

        }

    }
);

// Obtener elementos
const btnAyuda = document.getElementById("btnAyuda");
const modalAyuda = document.getElementById("modalAyuda");
const cerrarAyuda = document.getElementById("cerrarAyuda");
const cerrarAyuda2 = document.getElementById("cerrarAyuda2");

// Abrir ventana
btnAyuda.addEventListener("click", function() {
    modalAyuda.style.display = "block";
});

// Cerrar con la X
cerrarAyuda.addEventListener("click", function() {
    modalAyuda.style.display = "none";
});

// Cerrar con el botón Entendido
cerrarAyuda2.addEventListener("click", function() {
    modalAyuda.style.display = "none";
});

// Cerrar al hacer clic fuera de la ventana
window.addEventListener("click", function(event) {
    if (event.target === modalAyuda) {
        modalAyuda.style.display = "none";
    }
});

// Cerrar con la tecla Escape
document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
        modalAyuda.style.display = "none";
    }
});