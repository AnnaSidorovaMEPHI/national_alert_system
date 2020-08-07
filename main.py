from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
from mail import EmailSender

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')


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
