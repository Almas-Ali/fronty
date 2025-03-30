# Fronty Forms

Fronty provides a simple way to create HTML forms in Python. The powerful built-in form widget allows you to create forms with ease. You can create forms with different types, actions, methods, and elements. You can also add custom elements to the form. Not least, it provides a built-in styling to get started with your MVP faster.

## How to use a form

To use a form, you need to import it from the `fronty.html.widgets` module. For example, if you need to make a login form, you can use the `LoginForm` widget. You can simply call the `LoginForm` class and add it to your page.

There are different types of forms available in Fronty. You can import them from the `fronty.widgets.forms` module. The available forms are:

- `RegistrationForm`
- `LoginForm`
- `ContactForm`
- `SearchForm`
- `SubscribeForm`

```py linenums="1" title="main.py" hl_lines="16"
from fronty.widgets.forms import (
    RegistrationForm,
    LoginForm,
    ContactForm,
    SearchForm,
    SubscribeForm,
)

form_style: dict[str, str] = {
    'display': 'flex',
    'flex_direction': 'column',
    'justify_content': 'center',
    'align_items': 'center',
    'margin': '10px',
}

@app.route('/register')
def register():
    return (
        layout(
            html.Div(
                RegistrationForm(load_css=True)
            ).style(**form_style)
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
            ).style(**form_style)
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
            ).style(**form_style)
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
            ).style(**form_style)
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
            ).style(**form_style)
        )
        .add_title('Subscribe')
        .render()
    )
```
The full code is available in the [forms app][forms-app] example.


[forms-app]: https://github.com/Almas-Ali/fronty/blob/master/examples/widgets%20twicks/app2.py "Forms app"
