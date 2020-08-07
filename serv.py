#!/usr/bin/env python
from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
