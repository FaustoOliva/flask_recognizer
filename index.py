from flask import Flask, Response, request, render_template
from post.getAlumno import get_alumno
from machineLearning.CapturandoRostros import capturando
from machineLearning.Entrenandorf import crearModelo
from machineLearning.ReconocimientoFacial import reconocer


app = Flask(__name__)

legajoFinal = "d"

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/legajo", methods=["POST"])
def envioLegajo():
    legajo = request.form['legajo']
    legajoFinal = legajo
    while True:
        alumno = get_alumno(legajo)
    
        if alumno: 
            return render_template("alumno.html", alumno=alumno)

        else:
            return render_template("home.html", mensaje='No existe el legajo ingresado. Ingreselo de nuevo, tiene q aparentear así X0000')
    

@app.route("/respuesta", methods=["POST"])
def respuesta():
    respuesta = request.form['respuesta']

    if respuesta == 's':
        capturando(legajoFinal)
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


