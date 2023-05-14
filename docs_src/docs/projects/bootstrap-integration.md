# Bootstrap Integration

Now, let's integrate Bootstrap into our project. We will use the [Bootstrap CDN](https://getbootstrap.com/docs/5.3/getting-started/introduction/#css) to load the Bootstrap CSS and JavaScript files.

First, we will create a new folder named `components` inside the `project` folder. Then, we will create a new component named `layout.py` inside the `components` folder.

```py linenums="1" title="project/components/layout.py"
from fronty.html import *


def navbar(request, **data) -> Element:
    '''This is the navbar component'''

    # The navbar layout
    _layout = Nav(
        Div(
            Anchor(
                'Fronty',
                href='/',
            ).class_('navbar-brand'),
            Button(
                Element('span').class_('navbar-toggler-icon'),

            ).class_('navbar-toggler').attr('type', 'button').attr('data-bs-toggle', 'collapse').attr('data-bs-target', '#navbarScroll').attr('aria-controls', 'navbarScroll').attr('aria-expanded', 'false').attr('aria-label', 'Toggle navigation'),
            Ul(
                Li(
                    Anchor(
                        'Home',
                        href='/',
                    ).class_('nav-link active').attr('aria-current', 'page'),
                ).class_('nav-item'),
                Li(
                    Anchor(
                        'About',
                        href='/about',
                    ).class_('nav-link'),
                ).class_('nav-item'),
                Li(
                    Anchor(
                        'More',
                        href='#',
                    ).class_('nav-link dropdown-toggle').attr('role', 'button').attr('data-bs-toggle', 'dropdown').attr('aria-expanded', 'false'),
                    Ul(
                        Li(
                            Anchor(
                                'Action',
                                href='#',
                            ).class_('dropdown-item'),
                        ),
                        Li(
                            Anchor(
                                'Another action',
                                href='#',
                            ).class_('dropdown-item'),
                        ),
                        Li(
                            Element('hr').class_('dropdown-divider'),
                        ),
                        Li(
                            Anchor(
                                'Something else here',
                                href='#',
                            ).class_('dropdown-item'),
                        ),
                    ).class_('dropdown-menu'),
                ).class_('nav-item dropdown'),
            ).class_('navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll').attr('style', '--bs-scroll-height: 100px;'),
            Form(
                Input(
                    placeholder='Search',
                    aria_label='Search',
                ).class_('form-control me-2').attr('type', 'search'),
                Button(
                    'Search',
                ).class_('btn btn-outline-success').attr('type', 'submit'),
            ).class_('d-flex').attr('role', 'search'),

        ).class_('container-fluid'),
    ).class_('navbar navbar-expand-lg bg-body-tertiary')

    return _layout


def layout(request, **data) -> Html:
    '''This is the layout component'''

    # The main layout
    return Html(
        Head(
            Title('Fronty'),  # Page title
            Meta(charset='utf-8'),  # Character encoding
            # Responsive design
            Meta(name='viewport', content='width=device-width, initial-scale=1'),

            # Bootstrap CSS
            Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css',
                 integrity='sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD', crossorigin='anonymous'),
        ),

        Body(

            # Navbar
            navbar(request),

            # Main area of the page
            # The main area of the page is passed as a parameter to the layout component.
            # Get subcomponent from data or use default value
            data.get('content', 'Empty content'),

            # Bootstrap JS
            Script(src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js", integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN', crossorigin='anonymous'),
        ),
    )

```


Now, we will create a `index.py` file inside the `components` folder. This file will contain the home page component.

```py linenums="1" title="project/components/index.py"
from fronty.html import (
    Element,
    Div,
    H1,
    Text,
    Break
)

# components
from components.layout import layout


def home(request, **data) -> Element:
    '''This is the home page component'''

    _layout = layout(
        request=request,
        content=Div(
            H1('Home'),

            Text(
                f"""
                    Path: {request.path}
                    {Break()}
                    Method: {request.method}
                    
                """
            ),

        ).class_('container text-center')
    )

    return _layout


# We have added the about inside the index.py file for simplicity.
# You can create a new file for the about page component.
def about(request, **data) -> Element:
    '''This is the about page component'''

    _layout = layout(
        request=request,
        content=Div(
            H1('About'),
        ).class_('container text-center')
    )

    return _layout

```

Now, we will update the `app.py` file to use the new components.

```py linenums="1" title="project/app.py"
from flask import Flask, request
from fronty.html import *

# components
from components.index import home, about

app = Flask(__name__)


@app.route('/')
def index():
    '''This is the home page view function'''

    return home(
        request=request,
        title='A simple framework to build a website only with Python.',
    ).render()


@app.route('/about')
def about_view():
    '''This is the about page view function'''

    return about(
        request=request,
        title='A simple framework to build a website only with Python.',
    ).render()


if __name__ == '__main__':
    app.run(debug=True)

```

Now, we will run the project and open the home page in the browser.

```sh
python project/app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

Project URL: [Bootstrap Integration](https://github.com/Almas-Ali/fronty/tree/master/examples/Bootstrap%20integration)

![Bootstrap Integration](https://raw.githubusercontent.com/Almas-Ali/fronty/master/examples/Bootstrap%20integration/screenshot_1.png "Bootstrap Integration")

