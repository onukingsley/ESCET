from app import app, render_template
from flask_login import LoginManager , login_required, login_user, confirm_login, logout_user,current_user
from Function import *
from Config import *
from users import User
from flask import request as re ,redirect

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

    return render_template('Dashboard/index.html')

@app.route('/logout')
def logout():
    logout_user()
    return  redirect('/login')
@app.route('/check')
def check():
    user = current_user.get_id()
    return user

# @app.route('/signin', methods= ['POST'])
# def valid():
#     username = re.form.get('username')
#     password = re.form.get('password')
#     # password = re.form['password']
#
#     if checkempty([username, password]):
#         msg = "Fill all fields"
#     else:
#         msg = "Login Valid"
#     return msg
#




@app.route('/signin', methods=['POST'])
def sign():
    user = re.form.get('username')
    psword = re.form.get('password')
    remember = re.form.get('remember')
    # remember = re.form['remember']
    rem = False
    if remember:
        rem = True
    # user = re.args.get('username')
    # psword = re.args.get('pword')
    # return check(f"Username: {user}, Password: {psword}, {rem}")
    if checkempty([user,psword]):
        msg = "Fill all fields"
    else:
        result = select('admin','password', f"where username = '{user}'")

        if result:
            Dbpassword = result[0][0]
            if cr.verify(psword,Dbpassword) :
                me = loaduser(user)
                login_user(me)
                msg = "ok"
                # return redirect('/sign_in/<user>')
            else:
                msg= 'invalid login details'
        else:
            msg = 'user not found'
    return msg

