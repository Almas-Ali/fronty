from flask import Flask
from fronty.html import *
from fronty.css import *
from datetime import date

# CSS components

def style_css():
    '''This is the style component'''

    # The CSS() is used to create a CSS object.
    return CSS(

        # The Selector() is used to create a CSS selector.
        # Here we have used the universal selector to select all the elements.
        # *{} means select all the elements.
        # We have css properties inside the properties() method.
        # Passed the css properties as keyword arguments.
        # The properties() method returns a CSSProperties object.
        Selector('*').properties({
            'margin': '0',
            'padding': '0',
            'font-family': 'Roboto, sans-serif, Arial',
        }),

        # Here we have selected the body tag.
        # We have used the Selector('body') to select the body tag.
        # Selector('body').properties({}) is used to add css properties to the body tag.
        Selector('body').properties({
            'background-color': '#d6d6e7',
        }),
        Selector('nav').properties({
            'background-color': '#484c7a',
            'color': '#fff',
            'padding': '20px',
            'position': 'absolute',
            'width': '80%',
            'margin': '0 10%',
            'top': '10px',
            'border-radius': '12px'
        }),
        Selector('nav ul').properties({
            'list-style': 'none',
            'display': 'flex',
            'flex-direction': 'row',
            'justify-content': 'center',
        }),
        Selector('nav ul li').properties({
            'margin': '0 10px'
        }),
        Selector('a').properties({
            'text-decoration': 'none',
            'color': '#fff',
            'padding': '12px',
            'border-radius': '12px',
            'transition': 'all 0.3s ease-in-out',
            'font-size': '18px',
        }),
        Selector('nav a:hover').properties({
            'background-color': '#ddd',
            'color': 'black',
        }),
        Selector('nav a:active').properties({
            'background-color': '#4CAF50',
            'color': 'white',
        }),
        Selector('.container').properties({
            'margin': '90px 10%',
            'width': '80%',
            'text-align': 'center',
            'padding': '20px',
            'background-color': '#fff',
            'border-radius': '12px',
        }),
        Selector('footer').properties({
            'position': 'absolute',
            'bottom': '10px',
            'width': '80%',
            'margin': '0 10%',
            'border-radius': '12px',
            'text-align': 'center',
            'padding': '20px',
            'background-color': '#484c7a',
            'color': '#fff',
            'font-size': '12px',
        }),
    )


# Fronty components

def layout(request, **data):
    '''This is the layout component'''

    # The Html() is used to create a HTML object.
    return Html(
        Head(
            Title('Custom CSS Project'),
            Meta(charset='UTF-8'),
            Meta(content="IE=edge").attr('http-equiv', 'X-UA-Compatible'),
            Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
            Style(
                style_css().render(),
            ),
        ),
        Body(
            Nav(
                Ul(
                    Li(
                        Anchor('Home', href='/'),
                    ),
                    Li(
                        Anchor('About', href='/about'),
                    )
                )
            ),
            Div(
                H1(
                    'Custom CSS Project',
                ),
                Text(
                    'This is a custom CSS project using Fronty.',
                ),
            ).class_('container'),
            Footer(
                f'© {date.today().year} Fronty',
            ),
        )
    )


app = Flask(__name__)


@app.route('/')
def home():
    '''This is the home page view function'''

    # The render() method is used to convert the python objects to HTML string.
    return layout(
        request=None,
    ).render()


if __name__ == '__main__':
    app.run(debug=True)
