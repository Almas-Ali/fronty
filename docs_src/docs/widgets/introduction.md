# Widgets Introduction

## What is a widget?

A widget is a set of components that can be used to build a user interface (UI) smoothly and very quickly. Widgets are build for making development process easier and faster. Widgets are also used to make the UI more beautiful and attractive with a single line of code.

## How to use a widget?

To use a widget, you need to import it from the `fronty.html.widgets` module. For example, if you need to make a login form, you can use the `FormWidget` widget. You can simply call the `FormWidget` class and add it to your page.

```py linenums="1" title="main.py" hl_lines="16"
from fronty.html.widgets import FormWidget
from fronty.html import *

from flask import Flask

app = Flask(__name__)

@app.route("/")
def login():
   return Html(
        Head(
            Meta(charset="utf-8"),
            Title("Test case"),
        ),
        Body(
            FormWidget(load_css=True)
        )
    ).render()


if __name__ == "__main__":
    app.run(debug=True)
```
