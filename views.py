from flask import Flask, render_template, redirect, url_for, flash, request
from .forms import LoginForm, RegisterForm
from app import app,db
from werkzeug.security import check_password_hash,generate_password_hash
from .models import UserInfo
from flask_login import login_user,logout_user,current_user,login_required


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            user = UserInfo.query.filter_by(username=form.username.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('index'))

                flash('invalid credentials')

    return render_template("login.html", title="Login", form=form)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,method='sha256')
        username= form.username.data
        password= hashed_password
        email=form.email.data

        new_register = UserInfo(username=username, password=password, email=email)
        db.session.add(new_register)
        db.session.commit()
        flash('Registration was successful')

        return redirect(url_for('login'))




    return render_template('registration.html', form =form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))






@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html")
