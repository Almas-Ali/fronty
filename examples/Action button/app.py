from fronty.html import widgets
from fronty import (
    html,
    css,
    js
)

import flask

app = flask.Flask(__name__)


@app.route('/')
def page():
    def button_event_1(event, id):
        return js.Event(event, id=id)

    return html.Html(
        html.Head(
            html.Title('Action button'),
            html.Style(
                css.Selector('button').properties({
                    'padding': '10px',
                    'margin': '10px',
                    'font-size': '20px',
                    'cursor': 'pointer',
                    'background-color': 'lightblue',
                    'color': '#000',
                    'border': 'none',
                    'border-radius': '5px',
                }),
                css.Selector('button:hover').properties({
                    'background-color': 'lightgreen',
                }),
                css.Selector('.theme').properties({
                    'background-color': '#f0f0f0',
                    'color': '#000',
                }),
            ),
        ),
        html.Body(
            html.Div(
                html.Button('Click me', id='button1',
                            onclick="alert('Button clicked');"),
                html.Button('Python Click me', id='button2',
                            onclick=js.Alert('Python Alert')),
                # html.Button('Python Click me', id='button3', onclick=js.Event('click', id='button3')),
                # html.Button('Python Click me', id='button4', onclick=button_event_1('click', 'button4')),
                js.ConsoleLog('Hello world').script_wrap(),
                html.Button('Console log click', id='button5',
                            onclick=js.ConsoleLog('Python Console Log')),

                js.Function('squreNumber', ['x'],
                            js.ConsoleLog('x')).script_wrap(),
                js.SetTimeout('squreNumber(4)', 1000).script_wrap(),
            ),
        )
    ).render()


@app.route("/login", methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        print(flask.request.form)
        # print(widgets.FormWidget.get_form_data(flask.request.form))

    return html.Html(
        html.Head(
            html.Meta(charset="utf-8"),
            html.Title("Test case"),
        ),
        html.Body(
            widgets.FormWidget(
                load_css=True,
                method='POST',
                action='/login',
            ).add_element(
                html.Div(
                    html.Label('Mobile number')
                    .attr('for', 'mobile'),
                    html.Input(
                        type='phone',
                        name='mobile',
                        required="",
                        placeholder='Enter your mobile number',
                    )
                    .style(**{
                        'width': '100%',
                        'padding': '12px 20px',
                        'margin': '8px 0',
                        'display': 'inline-block',
                        'border': '1px solid #ccc',
                        'box-sizing': 'border-box',
                    }),
                ),
                first=True
            )
        )
    ).render()


if __name__ == '__main__':
    app.run(debug=True)
