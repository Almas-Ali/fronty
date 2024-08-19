from fronty import html
from fronty.html.templates import BasicTemplate
from fronty import css
from fronty.widgets.forms import (
    RegistrationForm,
    LoginForm,
    ContactForm,
    SearchForm,
    SubscribeForm,
)
from fronty.widgets.navs import NavWidget

from flask import Flask


app = Flask(__name__)


def style() -> css.CSS:
    '''This is the style of the page.'''

    return css.CSS(
        css.Selector('body').properties({
            'font-family': 'Noto Sans',
            'margin': '0',
            'padding': '0',
        }),
        css.Selector('.navbar').properties({
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'background-color': '#f1f1f1',
            'padding': '10px',
            'margin-bottom': '10px',
        }),
    )


def new_navbar() -> NavWidget:
    '''This is the navigation bar of the page.'''

    navbar = NavWidget(load_css=True)
    navbar.add_nav_link('Home', '/').add_style_last_element(
        color='black',
        font_size='16px',
        margin_right='15px'
    )
    navbar.add_nav_link('Register', '/register').add_style_last_element(
        color='blue',
        font_size='16px',
        margin_right='15px'
    )
    navbar.add_nav_link('Login', '/login').add_style_last_element(
        color='green',
        font_size='16px',
        margin_right='15px'
    )
    navbar.add_nav_link('Contact', '/contact').add_style_last_element(
        color='red',
        font_size='16px',
        margin_right='15px'
    )
    navbar.add_nav_link('Search', '/search').add_style_last_element(
        color='purple',
        font_size='16px',
        margin_right='15px'
    )
    navbar.add_nav_link('Subscribe', '/subscribe').add_style_last_element(
        color='brown',
        font_size='16px',
        margin_right='15px'
    )

    return navbar


def layout(*data) -> html.Html:
    '''This is the layout of the page.'''

    return (
        BasicTemplate(
            new_navbar(),
            *data
        )
        .add_style(style())
    )


@app.route('/')
def home():
    return layout(
        html.H1('Welcome to Fronty widgets example')
            .attr('align', 'center')
            .style(
                font_size='30px',
                font_family='Noto Sans',
        ),

        html.Text('This is a simple example of how to use Fronty widgets.')
        .attr('align', 'center'),
    ).render()


@app.route('/register')
def register():
    return (
        layout(
            html.Div(
                RegistrationForm(load_css=True)
            ).style(
                display='flex',
                flex_direction='column',
                justify_content='center',
                align_items='center',
                margin='10px',
            )
        )
        .add_title('Register')
        .render()
    )


@app.route('/login')
def login():
    return (
        layout(
            html.Div(
                LoginForm(load_css=True)
            ).style(
                display='flex',
                flex_direction='column',
                justify_content='center',
                align_items='center',
                margin='10px',
            )
        )
        .add_title('Login')
        .render()
    )


@app.route('/contact')
def contact():
    return (
        layout(
            html.Div(
                ContactForm(load_css=True)
            ).style(
                display='flex',
                flex_direction='column',
                justify_content='center',
                align_items='center',
                margin='10px',
            )
        )
        .add_title('Contact')
        .render()
    )


@app.route('/search')
def search():
    return (
        layout(
            html.Div(
                SearchForm(load_css=True)
            ).style(
                display='flex',
                flex_direction='column',
                justify_content='center',
                align_items='center',
                margin='10px',
            )
        )
        .add_title('Search')
        .render()
    )


@app.route('/subscribe')
def subscribe():
    return (
        layout(
            html.Div(
                SubscribeForm(load_css=True)
            ).style(
                display='flex',
                flex_direction='column',
                justify_content='center',
                align_items='center',
                margin='10px',
            )
        )
        .add_title('Subscribe')
        .render()
    )


if __name__ == '__main__':
    app.run(debug=True)
