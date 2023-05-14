# Starter Project

For simplicity, we have created a starter project that you can use to get started with your own project. It is a simple project that contains a single page with a single component. It is a good starting point for your own project.

```py linenums="1" title="starter_project/app.py"
from flask import Flask, request
from fronty.html import *

app = Flask(__name__)


def home(request) -> Html:
    '''This is the home page view function'''

    # The main HTML element.
    return Html(

        # The head tag contains the title and meta tags.
        Head(

            # The title tag contains the title of the page.
            Title('Home'),

            # The meta tags contain the meta information of the page.
            Meta(charset='utf-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1'),
        ),

        # The body tag contains all the content of the page.
        Body(

            # The center tag contains the main content of the page.
            # It is like using a HTML element when you don't know whats the name of a tag in fronty.
            # You can use the Element('tag') for this purpose.
            Element(
                'center',

                # The h1 tag contains the title of the page.
                H1(
                    'Welcome to Fronty!'
                ),
                
                # The Text() is used to add text to the page like paragraphs.
                Text(
                    'Fronty is a frontend web framework.'
                ),
            )
        )
    )


@app.route('/')
def index() -> str:
    '''This is the home page view function'''

    # The render() method is used to convert the python objects to HTML string.
    # The render() method returns a string. So, we can return it directly.
    return home(
        request=request,
    ).render()


if __name__ == '__main__':
    # Run the app in debug mode.
    # Learn more about Flask at https://flask.palletsprojects.com/en/2.1.x/
    app.run(debug=True)

```