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
    return Html(
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


def login_form() -> Element:
    '''This is the login form.'''
    return layout(
        Empty(
            FormWidget(
                load_css=True
            )
            .add_element(
                html.Empty(
                    html.H1('Login form')
                    .attr('align', 'center')
                    .style(font_size='30px', font_family='sans-serif')
                    .class_('form-title'),
                    html.Text('Please fill in this form to login.').class_(
                        'form-subtitle'),
                ),
                first=True
            )
            .add_element(
                html.Empty(
                    html.Anchor('Terms and conditions')
                    .attr('href', '#')
                    .style(color='blue', cursor='pointer', font_size='15px')
                ),
                first=False
            )
            .style(display='flex', flex_direction='row', justif_items='center')
            .render(),
        )
    )


@app.route('/')
def index():
    '''Widgets at a place'''
    return login_form().render()


@app.route('/test')
def test():
    return Html(
        Head(
            Meta(charset="utf-8"),
            Title("Test case"),
        ),
        Body(
            Div(
                Text(
                    'This is a paragraph.'
                )
            )
            .style(font_size='40px', font_family='sans-serif')
            .class_('container'),


            html.Div(
                html.Input()
                .attr('type', 'text')
                .attr('name', 'InputElement')
                .attr('value', 'InputValue')
                .attr('placeholder', 'InputPlaceholder')
                .required
                .readonly
                .disabled,
            ),

            Footer(
                Text(
                    'This is a footer.'
                )
            ).id('footer'),
        ),
    ).render()


if __name__ == '__main__':
    app.run(debug=True)
