from flask import Flask # importo la libreria flask es un framework para python que nos permite crear aplicaciones web de forma rapida y sencilla
from flask import render_template # importo la libreria render_template que nos permite renderizar plantillas html
from flaskext.mysql import MySQL # importo la libreria mysql que nos permite conectarnos a una base de datos mysql

app = Flask(__name__) # creo una instancia de la clase Flask

mysql = MySQL() # creo una instancia de la clase MySQL
app.config['MYSQL_DATABASE_USER'] = 'root' # configuro el usuario de la base de datos
app.config['MYSQL_DATABASE_PASSWORD'] = '' # configuro la contraseña de la base de datos
app.config['MYSQL_DATABASE_DB'] = 'movies_db' # configuro el nombre de la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # configuro el host de la base de datos

mysql.init_app(app) # inicializo la conexion a la base de datos

@app.route('/movies') # creo una ruta para la pagina principal
def index():

    sql = "INSERT INTO `movies_db`.`movies` (`created_at`,`updated_at`,`title`,`rating`,`awards`,`release_date`,`length`,`genre_id`) VALUES ( null, 'null','Pelicula de terror 1', 10.0,3, sysdate(), 120, 2);"
    conn = mysql.connect() # creo una conexion a la base de datos
    cursor = conn.cursor() # creo un cursor para realizar CRUD
    cursor.execute(sql) # ejecuto el insert en la base de datos
    conn.commit() # confirmo la transaccion

    return render_template('movies/index.html') # renderizo la plantilla index.html

if __name__ == '__main__': # si el archivo es el archivo principal
    app.run(host='0.0.0.0',port=4000,debug=True) # ejecuto la aplicacion
