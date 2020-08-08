import hashlib
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '192.168.88.167'
app.config['MYSQL_USER'] = 'archelik'
app.config['MYSQL_PASSWORD'] = 'bestpas5'
app.config['MYSQL_DB'] = 'archella'

mysql = MySQL(app)


@app.route('/registr', methods=['GET', 'POST'])  # ROUTE
def registration():
    if request.method == "POST":
        data = request.form
        id = 8
        id = int(data['id'])
        firstName = data['fname']
        lastName = data['lname']
        passport = data['']
        sity = data['sity']
        email = data['email']
        mobile = data['mobile']
        data_born = data['data_born']
        md5 = hashlib.md5(data['password']).hexdigest
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO People(id,firstName, lastName, passport, sity, email, mobile, data_born) VALUES (%i,%s,%s,%s,%s,%s,%s,%s)",
                    (id, firstName, lastName, passport, sity, email, mobile, data_born))
        cur.execute(
            "INSERT INTO Creds(id, email, password) VALUES (%i,%s,%s)", (id, email, md5))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])  # ROUTE
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)