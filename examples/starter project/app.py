from flask import Flask, request
from fronty.html import *

app = Flask(__name__)


def home(request) -> Html:
    '''This is the home page view function'''
    return Html(
        Head(
            Title('Home'),
            Meta(charset='utf-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1'),
        ),
        Body(
            Element(
                'center',
                Element(
                    'h1',
                    'Welcome to Fronty!'
                ),
                Element(
                    'p',
                    'Fronty is a frontend web framework.'
                ),
            )
        )
    )


@app.route('/')
def index() -> str:
    '''This is the home page view function'''
    return home(
        request=request,
    ).render()


if __name__ == '__main__':
    app.run(debug=True)
