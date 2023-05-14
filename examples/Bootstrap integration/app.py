from flask import Flask, request
from fronty.html import *

# components
from components.index import home, about

app = Flask(__name__)


@app.route('/')
def index():
    '''This is the home page view function'''

    return home(
        request=request,
        title='A simple framework to build a website only with Python.',
    ).render()


@app.route('/about')
def about_view():
    '''This is the about page view function'''

    return about(
        request=request,
        title='A simple framework to build a website only with Python.',
    ).render()


if __name__ == '__main__':
    app.run(debug=True)
