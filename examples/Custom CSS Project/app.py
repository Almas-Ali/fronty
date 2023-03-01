from flask import Flask
from fronty.html import *
from fronty.css import *
from datetime import date

# CSS components

def style_css():
    return CSS(
        Selector('*').properties({
            'margin': '0',
            'padding': '0',
            'font-family': 'Roboto, sans-serif, Arial',
        }),
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
            Element(
                'nav',
                Element(
                    'ul',
                    Element(
                        'li',
                        Anchor('Home', href='/'),
                    ),
                    Element(
                        'li',
                        Anchor('About', href='/about'),
                    )
                )
            ),
            Element(
                'div',
                Element(
                    'h1',
                    'Custom CSS Project',
                ),
                Element(
                    'p',
                    'This is a custom CSS project using Fronty.',
                ),
            ).class_('container'),
            Element(
                'footer',
                f'© {date.today().year} Fronty',
            ),
        )
    )


app = Flask(__name__)


@app.route('/')
def home():
    return layout(
        request=None,
    ).render()


if __name__ == '__main__':
    app.run(debug=True)
