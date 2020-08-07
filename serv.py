#!/usr/bin/env python
import smtplib
from flask import Flask, request, render_template, redirect, url_for, session
from flask_mail import Mail, Message as EmailMessage
import os

mail = Mail()
app = Flask(__name__)
mail.init_app(app)



@app.route('/profile')
def profile():
    data = dict(num=request.args.get('num'),
                chord=request.args.get('chord'))
    return render_template('profile.html', data=data)


@app.route('/')
def index():
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.starttls()
	smtpObj.login('archellik@gmail.com','smtp3228')
	smtpObj.sendmail('archellik@gmail.com',"Anna.Sidorova.1998@yandex.ru","go to bed!")
	smtpObj.quit()

	num = request.args.get('num')
	if num:
		return redirect(url_for('profile', num=int(num), chord='0'))
	return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)