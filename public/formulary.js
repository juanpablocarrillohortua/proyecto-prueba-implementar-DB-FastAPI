const form = document.getElementById('heroForm');
const mensaje = document.getElementById('mensaje');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Evita que la página se recargue

    // Recogemos los datos del formulario
    const heroData = {
        name: document.getElementById('name').value,
        secret_name: document.getElementById('secret_name').value,
        age: parseInt(document.getElementById('age').value) || null
    };

    try {
        // Enviamos los datos a la API (ajusta la URL si es necesario)
        const response = await fetch('https://proyecto-prueba-implementar-db-fastapi.onrender.com/heroes/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(heroData)
        });

        if (response.ok) {
            const result = await response.json();
            mensaje.innerText = `¡Éxito! Héroe guardado con ID: ${result.id}`;
            form.reset();
        } else {
            mensaje.innerText = "Error al guardar el héroe.";
            mensaje.style.color = "red";
        }
    } catch (error) {
        console.error("Error:", error);
        mensaje.innerText = "No se pudo conectar con el servidor.";
    }
});