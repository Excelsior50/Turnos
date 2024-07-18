from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Turno, Usuario
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    turnos = Turno.query.all()
    return render_template('admin.html', turnos=turnos)

@app.route('/registrar_turno', methods=['POST'])
def registrar_turno():
    data = request.json
    usuario = Usuario(nombre=data['nombre'], email=data['email'])
    turno = Turno(fecha=datetime.strptime(data['fecha'], '%Y-%m-%d %H:%M'), usuario=usuario)
    db.session.add(usuario)
    db.session.add(turno)
    db.session.commit()
    return jsonify({"mensaje": "Turno registrado", "comprobante": f"Comprobante de pago para {usuario.nombre}"})

@app.route('/cambiar_turno', methods=['POST'])
def cambiar_turno():
    data = request.json
    turno = Turno.query.get(data['turno_id'])
    nueva_fecha = datetime.strptime(data['nueva_fecha'], '%Y-%m-%d %H:%M')
    if (turno.fecha - datetime.now()).days >= 2:
        turno.fecha = nueva_fecha
        db.session.commit()
        return jsonify({"mensaje": "Turno cambiado"})
    else:
        return jsonify({"mensaje": "No se puede cambiar el turno con menos de 48 horas de antelación"})

@app.route('/configurar_turnos', methods=['POST'])
def configurar_turnos():
    data = request.json
    # Lógica para configurar turnos disponibles
    return jsonify({"mensaje": "Turnos configurados"})

if __name__ == '__main__':
    app.run(debug=True)
