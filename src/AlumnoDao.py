import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Alumno:
	idalumno = 0
	nombres = ""
	apellidos = ""
	codigo = ""
	correo = ""
	def readAll(self):
		try:
			conexion = cx.conecta()
			cursor = conexion.cursor(pymysql.cursors.DictCursor)
			cursor.callproc('sp_listar_alumno')
			rows = cursor.fetchall()
			return rows
		except Exception as e:
			print(e)
			
		finally:
			cursor.close()
			conexion.close()
	def delete(self):
		try:
			conexion = cx.conecta()
			cursor = conexion.cursor()
			cursor.callproc("sp_eliminar_alumno", [self.idalumno,])
			conexion.commit()
			return 1
		except Exception as e:
			print(e)
		finally:
			cursor.close() 
			conexion.close()
	def update(self):
		try:
			_id = self.idalumno
			_nombre = self.nombres
			_apellido = self.apellidos
			_codigo = self.codigo
			_correo = self.correo
			data = [ _id, _nombre, _apellido, _codigo, _correo]
			conexion = cx.conecta()
			cursor = conexion.cursor(pymysql.cursors.DictCursor)
			cursor.callproc("sp_editar_alumno",data)
			conexion.commit()
			return 1
		except Exception as e:
			print(e)
		finally: 
			cursor.close()
			conexion.close()
	def create(self):
		try:
			_nombre = self.nombres
			_apellido = self.apellidos
			_codigo = self.codigo
			_correo = self.correo
			data = [ _nombre, _apellido, _codigo, _correo]
			conexion = cx.conecta()
			cursor = conexion.cursor(pymysql.cursors.DictCursor)
			cursor.callproc("sp_create_alumno",data)
			conexion.commit()
			return 1
		except Exception as e:
			print(e)
		finally: 
			cursor.close()
			conexion.close()