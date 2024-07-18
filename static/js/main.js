function registrarTurno() {
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    const fecha = document.getElementById('fecha').value;

    fetch('/registrar_turno', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre, email, fecha })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensaje').innerText = data.mensaje;
    })
    .catch(error => console.error('Error:', error));
}
