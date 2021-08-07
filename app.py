from flask import Flask, render_template
from Function import *
from Config import *

app = Flask(__name__)

app.debug = True
@app.context_processor
def details():
    pageinformation = {
        'menu' : menu
    }
    return dict(pd=page_details, replacer=replacer , info=pageinformation)


@app.route('/about')
def hello_world():
    pageinfo = {
        'title' : 'about us',
        'sub' : 'college of education enugu (technical) is an instutition built on knowledge and hardwork'
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
    pageinfo = {
        'title': 'Welcome',

    }
    return render_template('index1.html', pg=pageinfo)

@app.route('/courses')
def courses():
    pageinfo = {
        'title': 'courses',
        'sub': 'so many courses to learn, there is no limit to learning'
    }
    return render_template('courses.html', pg=pageinfo)

@app.route('/admission')
def admission():
    pageinfo = {
        'title': 'admission',
        'sub': 'our addmission is available now'
    }
    return render_template('admissions.html',pg=pageinfo)

if __name__ == '__main__':
    app.run(debug=True)
