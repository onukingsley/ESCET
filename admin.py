from app import app, render_template
from flask_login import LoginManager , login_required, login_user, confirm_login, logout_user,current_user
from Function import *
from Config import *
from users import User
from flask import request,redirect

loginManager = LoginManager(app)

@loginManager.user_loader
def loaduser(username):
    return User(username)

@app.route("/dashboard")
@login_required
def dashboard():
    pageinfo= {

    }
    return render_template('Dashboard/index.html',pg=pageinfo)

@app.route('/sign_in/<user>')
def sign_in(user):
    me = loaduser(user)
    login_user(me)
    return render_template('Dashboard/index.html')

@app.route('/logout')
def logout():
    logout_user()
    return  redirect('/login')
@app.route('/check')
def check():
    user = current_user.get_id()
    return user






