from flask import Flask, request
from flask import jsonify
import tools.sql_tools as sqt

app = Flask(__name__)

"""API GET"""

@app.route("/")
def inicio():
    return "bienvenido a mi api"


@app.route("/personajes")
def damelos():
    persons = sqt.personajes()
    return jsonify(persons)

@app.route("/dialogos")
def damelos1():
    dial = sqt.dialogos()
    return jsonify(dial)

@app.route("/frases/<personaje>")
def frases(personaje):
    frasecitas = sqt.dialogo_persona(personaje)
    return jsonify(frasecitas)

"""API POST"""
@app.route("/nuevafrase/<personaje>")

@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    dia = request.form.get("frase")
    person = request.form.get("personaje")
    tempor = request.form.get("tempo")
    # PODRÍAMOS LLAMAR A FUNCIONES CHECK
    print(scene, char_, dialogue)

    return sqt.nuevomensaje(dia, person, tempor)













app.run(debug=True)