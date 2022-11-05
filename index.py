from flask import Flask, session, request, render_template
from post.getAlumno import get_alumno
from machineLearning.CapturandoRostros import capturando
from machineLearning.Entrenandorf import crearModelo
from machineLearning.ReconocimientoFacial import reconocer


app = Flask(__name__)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/legajo", methods=["POST"])
def envioLegajo():
    legajo = request.form['legajo']
    session['legajoFinal'] = legajo
    while True:
        alumno = get_alumno(legajo)
    
        if alumno: 
            return render_template("alumno.html", alumno=alumno)

        else:
            return render_template("home.html", mensaje='No existe el legajo ingresado. Ingreselo de nuevo, tiene q aparentear así X0000')
    

@app.route("/respuesta", methods=["POST"])
def respuesta():
    respuesta = request.form['respuesta']
    legajo = session.get('legajoFinal', None)
    if respuesta == 's':
        capturando(legajo)
        return render_template("entrenamiento.html")
    elif respuesta == 'n':
        return render_template("home.html", error='Alumno incorrecto. Ingreselo de nuevo, tiene q aparentear así X0000')


@app.route("/modelo", methods=["POST"])
def modelo():
    crearModelo()
    reconocer()
    return render_template("reconocimiento.html")



if __name__ == "__main__":
    app.run(debug=True)


