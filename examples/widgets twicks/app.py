from fronty.html import *
from fronty.html.widgets import *
from fronty.css import *

from flask import Flask

app = Flask(__name__)


def style() -> Element:
    '''This is the style of the page.'''
    return CSS(
        Selector('.container').properties({
            'margin': '0 auto',
            'width': '50%',
            'border': '1px solid #ccc',
            'padding': '10px',
            'border': '2px solid #000'
        })
    )


def layout(data: Element) -> Element:
    '''This is the layout of the page.'''
    return (
        Html(
            Head(
                Meta(charset="utf-8"),
                Title("Fronty widgets example"),
                # Style(
                #     style().render()
                # ),
            ),
            Body(
                Div(
                    data,
                ).class_("container"),
            ),
        )
    )


def login_form() -> Element:
    '''This is the login form.'''
    return layout(
        Div(
            FormWidget(
                load_css=True,
                action='#',
                method='post'
            ).render()
        ).class_('form-tags'),
    )


@app.route('/')
def index():
    '''Widgets at a place'''
    return login_form().render()


if __name__ == '__main__':
    app.run(debug=True)
