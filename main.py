import hashlib
import flask
from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
from flask_mysqldb import MySQL 
from mail import EmailSender

app = Flask(__name__)
app.config['MYSQL_HOST'] = '192.168.88.167'
app.config['MYSQL_USER'] = 'archelik'
app.config['MYSQL_PASSWORD'] = 'bestpas5'
app.config['MYSQL_DB'] = 'archella'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == "GET":
            return render_template('login.html')
        if request.method == "POST":
            data = request.form
            email=data['login']
            password = data['password']
            md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
            cur = mysql.connection.cursor()
            # SQLi, but I have not time to fix it :))
            query_string = "SELECT Hash FROM Creds WHERE Email = %s"
            cur.execute(query_string, (email,))
            true_hash = cur.fetchone()[0]
            if true_hash == md5:
                return cabinet(email)
            else:
                return "Неверный логин или пароль."
        if request.method == "GET":
            return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])  ###  ROUTE
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        data = request.form
        id = 15
        # id = int(data['id'])
        firstName = data['firstName']
        lastName = data['lastName']
        passport = data['passport']
        city=data['city']
        email=data['login']
        mobile = data['phone']
        data_born= data['birthDate']
        pas = data['password']
        md5 = hashlib.md5(pas.encode('utf-8')).hexdigest()
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO People(Chell_ID,  Name_Chell, Surname, Pass_nomer, City, Email, Phone_number, Birthday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                        (id, firstName, lastName, passport, city, email, mobile, data_born))
            cur.execute(
                "INSERT INTO Creds(Chell_ID, Email, Hash) VALUES (%s,%s,%s)", (id, email, md5))
            mysql.connection.commit()
            cur.close()
        except Exception:
            return 'Зарегистрироваться не удалось.' + str(e)
        return cabinet(email)


@app.route('/cabinet')
def cabinet(email=None):
    if email:
        cur = mysql.connection.cursor()
        try:
            query_string = "SELECT Name_Chell FROM People WHERE Email = %s"
            cur.execute(query_string, (email,))
            name = cur.fetchone()[0]
            return render_template('cabinet.html', name=name)
        except:
            return flask.abort(404)
    else:
        return flask.abort(404)


@app.route('/styles/<path:path>')
def styles(path):
    return send_from_directory('styles', path)


@app.route('/scripts/<path:path>')
def scripts(path):
    return send_from_directory('scripts', path)


@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)


@app.route('/mail')
def mail():
    mail = EmailSender(["archellik@gmail.com"])
    mail.send_alert(r"Добрый день.Убедительная просьба явиться на вакцинацию!".encode(
        'utf-8', errors='ignore'))
    return render_template('index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
