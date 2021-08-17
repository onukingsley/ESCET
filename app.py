from flask import Flask, render_template
from Function import *
from Config import *

app = Flask(__name__)




@app.context_processor
def details():
    pageinformation = {
        'menu': menu,
        'header': header,
    }
    return dict(pd=page_details, replacer=replacer, info=pageinformation)


@app.route('/about')
def hello_world():
    pageinfo = {
        'title': 'about us',
        'sub': 'college of education enugu (technical) is an instutition built on knowledge and hardwork'

    }
    return render_template('about.html', pg=pageinfo)


@app.route('/contact')
def contact():
    pageinfo = {
        'title': 'contact',
        'sub': 'Contact us today to get the best learning experience'
    }
    return render_template('contact1.html', pg=pageinfo)


@app.route('/')
def index():
    try:
        url = 'https://newsapi.org/v2/top-headlines?country=ng&category=science&apiKey=819b3b2ae72f4ed48335a601245879c9'
        news = request('GET', url)
        news = json.loads(news.content)
        result = news['articles']

    except Exception as err:
        print(err)
    pageinfo = {
        'title': 'Welcome',
        'news': result,
    }
    return render_template('index1.html', pg=pageinfo)


@app.route('/courses')
def courses():
    pageinfo = {
        'title': 'courses',
        'sub': 'so many courses to learn, there is no limit to learning'
    }
    return render_template('courseds.html', pg=pageinfo)


@app.route('/admission')
def admission():
    pageinfo = {
        'title': 'admission',
        'sub': 'our addmission is available now'
    }
    return render_template('admissions.html', pg=pageinfo)


@app.route('/register')
def register():
    pageinfo = {
        'title': 'Register',
        'sub': 'our addmission is available now'
    }
    return render_template('register.html', pg=pageinfo)


@app.route('/login')
def login():
    pageinfo = {
        'title': 'Admission',
        'sub': 'our addmission is available now'
    }
    return render_template('register.html', pg=pageinfo)


# ERROR HANDLING
@app.errorhandler(404)
@app.route("/404")
def error404(error=''):
   return render_template('Dashboard/error_400.html')

@app.errorhandler(500)
@app.route("/500")
def error500(error=''):
   return render_template('Dashboard/error_500.html')

@app.errorhandler(401)
@app.route("/401")
def error401(error=''):
   return render_template('Dashboard/error_401.html')


from admin import *

if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
