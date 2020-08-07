#!/usr/bin/env python
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)

@app.route('/profile')
def profile():
    data = dict(num=request.args.get('num'),
                chord=request.args.get('chord'))
    return render_template('profile.html', data=data)


@app.route('/')
def index():
    num = request.args.get('num')
    if num:
        return redirect(url_for('profile', num=int(num), chord='0'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)