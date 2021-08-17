from app import app, render_template
from flask_login import LoginManager , login_required, login_user, confirm_login, logout_user
from Function import *
from Config import *
from users import User

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


