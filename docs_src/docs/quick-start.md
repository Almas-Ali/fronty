# Quick Start

As fronty is a very simple framework, it is very easy to use. You can easily create a website using. It
is mainly focused on the frontend part. So, we haven't add any backend features. But, you can easily add
backend features using any backend framework like Flask, Django, etc.

But, we are working on a backend framework for fronty named [Backkr][backkr]. And we are also
working on a database framework named [Flexdb][flexdb]. So, you can easily create a full stack
website with database using [Fronty][fronty] in only Python technology without knowing any kind
of web technologies like HTML, CSS, and JavaScript.

Here we will use flask as a backend framework for making this documentation short. But, you can use any
backend framework you want. We will update this documentation when we release [Backkr][backkr] and [Flexdb][flexdb]. So, you can easily create a full stack website using only Python.

## Starter template

```py linenums="1" title="app.py"
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

```

This is a starter template for fronty. You can use this template to create a basic website using
fronty.
<br>
First, we import the Flask and request from flask. Then, we import Html, Head, Title, Meta, Body,
Element from fronty.html package.
<br>
Then, we create a flask app. Then, we create a home view function. This view function will return
a Html object. This Html object will contain the HTML code for the home page.
<br>
Then, we create a index view function. This view function will call the home view function and
render the HTML code.
<br>
Then, we run the flask app.

**Fronty** has a very simple syntax. You can easily create a website using it. It has
some built-in element like **Button, Link, Anchor** etc. You can use these elements to
create a website. You can also create your own element using the **BaseElement** class.
We will see how to create a element in the customization section.

[backkr]: https://github.com/Almas-Ali/backkr "Backkr"
[flexdb]: https://github.com/Almas-Ali/flexdb "Flexdb"
[fronty]: https://github.com/Almas-Ali/fronty "Fronty"
