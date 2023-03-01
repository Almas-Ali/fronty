# Fronty - A frontend web framework

Created by [**@Almas-Ali**](https://github.com/Almas-Ali)

Learn from the official [**`Documentation`**](https://almas-ali.github.io/fronty/)

## Table of Contents

- [What is Fronty?](#what-is-fronty)
- [Installation](#installation)
- [Example Projects](#example-projects)
- [How to run the example projects](#how-to-run-the-example-projects)
- [How to create a new project](#how-to-create-a-new-project)
- [Contributing](#contributing)

## What is Fronty?

Fronty is a frontend web framework. It is a Python library that allows you to create web pages using only Python. No HTML, CSS, or JavaScript required. But you can still use them if you want. Basic knowledge of HTML, CSS, and JavaScript is required to use Fronty.

## Installation

Easy to install with pip.

```bash
pip install fronty
```

## Example Projects

[**`Starter Project`**](https://github.com/Almas-Ali/fronty/tree/master/examples/starter%20project)

![Screenshort_1](https://raw.githubusercontent.com/Almas-Ali/fronty/master/examples/starter%20project/screenshot_1.png "Starter Project Screenshot 1")

[**`Bootstrap Integration`**](https://github.com/Almas-Ali/fronty/tree/master/examples/Bootstrap%20integration)

![Screenshort_1](https://raw.githubusercontent.com/Almas-Ali/fronty/master/examples/Bootstrap%20integration/screenshot_1.png "Bootstrap Integration Screenshot 1")

[**`Custom CSS Project`**](https://github.com/Almas-Ali/fronty/tree/master/examples/Custom%20CSS%20project)

![Screenshort_1](https://raw.githubusercontent.com/Almas-Ali/fronty/master/examples/Custom%20CSS%20Project/screenshot_1.png "Custom CSS Project Screenshot 1")

![Screenshort_2](https://raw.githubusercontent.com/Almas-Ali/fronty/master/examples/Custom%20CSS%20Project/screenshot_2.png "Custom CSS Project Screenshot 2")

## How to run the example projects

1. Clone the repository

```bash
git clone https://github.com/Almas-Ali/fronty.git
```

2. Go to the example project directory

```bash
cd fronty/examples/starter\ project
```

3. Run the project

```bash
python app.py
```

**Note:** You have to install a backend server to run the project. Fronty does not provide a backend server. You can use any backend server you want. For example, you can use Flask. You can also use Fronty with Django. But you have to install Django first. For simplicity, we have used Flask in the example projects. We are woring on a backend server for Fronty. It will be available soon.

## How to create a new project

1. Create a new directory

```bash
mkdir my_project
```

2. Go to the directory

```bash
cd my_project
```

3. Create a new file named `app.py`

```bash
touch app.py
```

4. Open the file with your favorite text editor

5. Copy the following code and paste it in the file

```python
from flask import Flask, request
from fronty.html import *

app = Flask(__name__)


def home(request) -> Html:
    '''This is the home page view function'''
    return Html(
        Head(
            Title('Home'),
            Meta(charset='utf-8'),
            Meta(name='viewport', content='width=device-width, initial-scale=1'),
        ),
        Body(
            Element(
                'center',
                Element(
                    'h1',
                    'Welcome to Fronty!'
                ),
                Element(
                    'p',
                    'Fronty is a frontend web framework.'
                ),
            )
        )
    )


@app.route('/')
def index() -> str:
    '''This is the home page view function'''
    return home(
        request=request,
    ).render()


if __name__ == '__main__':
    app.run(debug=True)
```

6. Run the project

```bash
python app.py
```

7. Open the browser and go to `http://127.0.0.1:5000/`

![Screenshort_1](https://raw.githubusercontent.com/Almas-Ali/fronty/master/examples/starter%20project/screenshot_1.png "Starter Project Screenshot 1")

## Contributing

Pull requests are welcome. For any changes, please open an issue first to discuss what you would like to change.

**Thanks for using Fronty!**
