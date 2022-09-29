from flask import Flask, Response, request, render_template
from post.getAlumno import get_alumno
from machineLearning.CapturandoRostros import capturando
from machineLearning.Entrenandorf import crearModelo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/legajo", methods=["POST"])
def envioLegajo():
    legajo = request.form['legajo']

    if legajo == 's':
        ejecutarReconocimiento(legajo)
    elif legajo == 'n':
        return render_template("home.html", error='Alumno incorrecto. Ingreselo de nuevo, tiene q aparentear así X0000')

    else:      
        while True:
            alumno = get_alumno(legajo)
        
            if alumno: 
                return render_template("alumno.html", alumno=alumno)

            else:
                return render_template("home.html", mensaje='No existe el legajo ingresado. Ingreselo de nuevo, tiene q aparentear así X0000')
    
def ejecutarReconocimiento(legajo):
    capturando(legajo)
    return render_template("entrenamiento.html")

@app.route("/modelo", methods=["POST"])
def moedlo():
    crearModelo()


if __name__ == "__main__":
    app.run(debug=True)


