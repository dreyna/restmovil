import pymysql
class Conexion:
    def __init__(self):
        self._ServidorDB = "localhost"
        self._UsuarioDB = "root"
        self._PasswordDB = "root"
        self._BD = "bdrest"
    def conecta(self):
        db = pymysql.connect(self._ServidorDB, self._UsuarioDB, self._PasswordDB,self._BD,port=3306)
        print("onexion exitosa...")
        return db
cx = Conexion()
print(cx.conecta())