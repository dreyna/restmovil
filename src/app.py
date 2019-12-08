from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from AlumnoDao import Alumno
app = Flask(__name__)
@app.route('/alumnos/listar', methods=['GET'])
def listar():
	try:
		rows = alum.readAll()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
@app.route('/alumnos/delete/<int:id>', methods=['DELETE'])
def eliminarAlumno(id):
	try:
		alum.idalumno=id
		resp = alum.delete()
		resp = jsonify('Alumno eliminado')
		resp = make_response(jsonify({"message": "Collection replaced"}), 200)
		return resp
	except Exception as e:
		print(e)
@app.route('/alumnos/update/<int:id>', methods=['PUT'])
def update(id):
	try:
		_json = request.json
		alum.idalumno = id
		alum.nombres = _json['nombres']
		alum.apellidos = _json['apellidos']
		alum.codigo = _json['codigo']
		alum.correo = _json['correo']
		if request.method == 'PUT':
			resp = alum.update()
			resp = make_response(jsonify({"message": "Collection replaced"}), 200)
			return resp
	except Exception as e:
		print(e)
@app.route('/alumnos/create', methods=['POST'])
def crear():
	try:
		_json = request.json
		alum.nombres = _json['nombres']
		alum.apellidos = _json['apellidos']
		alum.codigo = _json['codigo']
		alum.correo = _json['correo']
		if request.method == 'POST':
			resp = alum.create()
			resp = make_response(jsonify({"message": "Collection replaced"}), 200)
			return resp
	except Exception as e:
		print(e)
if __name__=="__main__":
	alum = Alumno()
	app.run(host="0.0.0.0", port=5000, debug=True)
