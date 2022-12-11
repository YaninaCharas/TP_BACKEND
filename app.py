# importo la libreria flask es un framework para python que nos permite crear aplicaciones web de forma rapida y sencilla
from flask import Flask
# importo la libreria render_template que nos permite renderizar plantillas html
from flask import render_template, request
# importo la libreria mysql que nos permite conectarnos a una base de datos mysql
from flaskext.mysql import MySQL

# Jinja2 es un motor de plantillas que nos permite crear plantillas html dinamicas

app = Flask(__name__)  # creo una instancia de la clase Flask

mysql = MySQL()  # creo una instancia de la clase MySQL
# configuro el usuario de la base de datos
app.config['MYSQL_DATABASE_USER'] = 'root'
# configuro la contraseña de la base de datos
app.config['MYSQL_DATABASE_PASSWORD'] = ''
# configuro el nombre de la base de datos
app.config['MYSQL_DATABASE_DB'] = 'movies_db'
# configuro el host de la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)  # inicializo la conexion a la base de datos


@app.route('/')  # creo una ruta para la pagina principal
def index():

    # creo una consulta sql para obtener todas las peliculas
    sql = "SELECT * FROM `movies_db`.`movies`"

    conn = mysql.connect()  # creo una conexion a la base de datos
    cursor = conn.cursor()  # creo un cursor para realizar CRUD
    cursor.execute(sql)  # ejecuto la consulta en la base de datos
    data_movies = cursor.fetchall()  # obtengo los datos de la consulta
    conn.commit()  # confirmo la transaccion

    # renderizo la plantilla index.html
    return render_template('movies/index.html', movies=data_movies)


@app.route('/create')  # creo una ruta para la pagina de creacion de peliculas
def create():
    return render_template('movies/create.html')


# creo una ruta para la pagina de creacion de peliculas
@app.route('/store', methods=['POST'])
def storage():
    # Recibo los datos del formulario de creacion de peliculas
    # obtengo el valor del input con el name inputName
    _name = request.form['name']
    # obtengo el valor del input con el name inputRating
    _rating = request.form['rating']
    # obtengo el valor del input con el name inputAwards
    _awards = request.form['awards']
    # obtengo el valor del input con el name inputLength
    _length = request.form['length']
    # obtengo el valor del input con el name inputGenreId
    _genre_id = request.form['genre_id']

    sql = "INSERT INTO `movies_db`.`movies` (`created_at`,`updated_at`,`title`,`rating`,`awards`,`release_date`,`length`,`genre_id`) VALUES ( sysdate(), sysdate(),'" + \
        _name + "', " + _rating + ", " + _awards + ", sysdate()," + _length + \
        ", " + _genre_id + ");"

    conn = mysql.connect()  # creo una conexion a la base de datos
    cursor = conn.cursor()  # creo un cursor para realizar CRUD
    cursor.execute(sql)  # ejecuto el insert en la base de datos
    conn.commit()  # confirmo la transaccion

    return 'Pelicula creada con exito'


# creo una ruta para la pagina de eliminacion de peliculas
@app.route('/delete/<id>')
def delete(id):

    sql = "DELETE FROM `movies_db`.`movies` WHERE `id` = " + id + ";"
    conn = mysql.connect()  # creo una conexion a la base de datos
    cursor = conn.cursor()  # creo un cursor para realizar CRUD
    cursor.execute(sql)  # ejecuto el delete en la base de datos
    conn.commit()  # confirmo la transaccion

    return 'Pelicula eliminada con exito'


# creo una ruta para la pagina de edicion de peliculas
@app.route('/edit/<id>')
def edit(id):

    sql = "SELECT * FROM `movies_db`.`movies` WHERE `id` = " + id + ";"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    data_movie = cursor.fetchone()
    conn.commit()

    return render_template('movies/edit.html', movie=data_movie)


# creo una ruta para la pagina de edicion de peliculas
@app.route('/update', methods=['POST'])
def update():

    _id = request.form['movie_id']
    _name = request.form['name']
    _rating = request.form['rating']
    _awards = request.form['awards']
    _length = request.form['length']
    _genre_id = request.form['genre_id']

    sql = "UPDATE `movies_db`.`movies` SET `updated_at` = sysdate(), `title` = '" + _name + "', `rating` = " + _rating + ", `awards` = " + _awards + ", `length` = " + _length + ", `genre_id` = " + _genre_id + " WHERE (`id` = " + _id + ");"

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return 'Pelicula actualizada con exito'


if __name__ == '__main__':  # si el archivo es el archivo principal
    app.run(host='0.0.0.0', port=4000, debug=True)  # ejecuto la aplicacion




if __name__ == '__main__': # si el archivo es el archivo principal
    app.run(host='0.0.0.0',port=4000,debug=True) # ejecuto la aplicacion
