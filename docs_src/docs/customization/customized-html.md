# Customizing Components

You can customize the built-in components or create your own components by subclassing the `fronty.html.BaseElement` class. Let's see how to create a custom component.

```py linenums="1" title="custom_components.py" hl_lines="11 12 14 15 16 17"

from fronty.html import (
    BaseElement,
    Text
)


class CustomComponent(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('custom-component', *children, **attributes)

        # Optional attributes if you want to add any custom attributes
        self._attributes['custom-attribute'] = 'custom-value'

        # Optional children if you want to add any custom children
        self._children = [
            Text('This is a custom component.'),
        ]

```

Now, you can use this component in your application.

```py linenums="1" title="main.py"
from flask import Flask # or any other framework
from fronty.html import (
    Html,
    Head,
    Title,
    Body,
)
from custom_components import CustomComponent # import the custom component

app = Flask(__name__)

def layout():
    return Html(
        Head(
            Title('Custom Component')
        ),
        Body(
            CustomComponent()
        )
    )


@app.route('/')
def home():
    return layout().render()
    

if __name__ == '__main__':
    app.run(debug=True)


```
