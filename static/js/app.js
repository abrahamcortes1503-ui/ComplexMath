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