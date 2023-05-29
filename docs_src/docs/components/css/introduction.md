# CSS Components

## What are CSS Components?

CSS components are a list of dictionary that can be used to create a CSS styling fast and easily. These components are very easy to use and can be used to create a CSS styling in a few lines of code. Here is lots of customization options are available. Let's get started.

## Important CSS Components

`CSS` : To create a css in a html website.

`Selector` : To create a selector in a html website. It is like query selector in JavaScript.

`Style` : To create a style in a html website.

## Using CSS Components

To use CSS components, you have to import the `fronty.css` module methods. `CSS`, `Selector` and `Style` are the methods of `fronty.css` module. Here is an example of using `fronty.css` module methods:

```py linenums="1" title="Example of importing fronty.css module" hl_lines="3 4 5"
from fronty.css import CSS, Selector, Style

css = CSS(
    Selector('body')
)

print(css.render())
```

With this you can create a selector in a html website. But it is not enough to create a css file. You have to add some properties to the selector. To add properties to the selector, you have to use the `properties` attribute of the `Selector` element. Here is an example:

```py linenums="1" title="Example of properties attribute" hl_lines="5 6 7 8 9 10 11 12 13"
from fronty.css import CSS, Selector, Style

css = CSS(
    Selector('body')
    .properties({
        "background-color": "red",
        "color": "white",
        "font-size": "20px",
        "font-weight": "bold",
        "padding": "10px",
        "border-radius": "5px",
        "border": "1px solid black"
    })
)

print(css.render())
```

Output:

```css linenums="1" title="Output of the above code"
body{background-color:red;color:white;font-size:20px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}
```

Here we have provided a dictionary in `properties` method of `Selector` class. The keys of the dictionary are the properties of the CSS component and the values of the dictionary are the values of the properties. You can add as many properties as you want. You can also add multiple selectors in a CSS file. Here is an example:

```py linenums="1" title="Example of multiple selectors" hl_lines="4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22"
from fronty.css import CSS, Selector, Style

css = CSS(
    Selector('body')
    .properties({
        "background-color": "red",
        "color": "white",
        "font-size": "20px",
        "font-weight": "bold",
        "padding": "10px",
        "border-radius": "5px",
        "border": "1px solid black"
    }),
    Selector('h1')
    .properties({
        "color": "blue",
        "font-size": "30px",
        "font-weight": "bold",
        "padding": "10px",
        "border-radius": "5px",
        "border": "1px solid black"
    })
)

print(css.render())
```

Output:

```css linenums="1" title="Output of the above code"
body{background-color:red;color:white;font-size:20px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}h1{color:blue;font-size:30px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}
```

You can also add multiple properties in a selector. Here is an example:

```py linenums="1" title="Example of multiple properties" hl_lines="5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21"
from fronty.css import CSS, Selector, Style

css = CSS(
    Selector('body')
    .properties({
        "background-color": "red",
        "color": "white",
        "font-size": "20px",
        "font-weight": "bold",
        "padding": "10px",
        "border-radius": "5px",
        "border": "1px solid black"
    })
    .properties({
        "color": "blue",
        "font-size": "30px",
        "font-weight": "bold",
        "padding": "10px",
        "border-radius": "5px",
        "border": "1px solid black"
    })
)

print(css.render())
```

Output:

```css linenums="1" title="Output of the above code"
body{background-color:red;color:blue;font-size:30px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}
```

Here we can see, only the unique properties are added to the selector and the duplicate properties are overwritten with the new properties.

## Using Style Component

You can also use the `Style` component to create a CSS file. Here is an example:

```py linenums="1" title="Example of Style component" hl_lines="5 6"
from fronty.css import CSS, Selector
from fronty.html import Style

css = CSS(
    Style('body{background-color:red;color:white;font-size:20px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}'),
    Style('h1{color:blue;font-size:30px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}')
)

print(css.render())
```

Output:

```css linenums="1" title="Output of the above code"
<style type="text/css" href="" rel="stylesheet">body{background-color:red;color:white;font-size:20px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}</style><style type="text/css" href="" rel="stylesheet">h1{color:blue;font-size:30px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}</style>
```

This is very unrealistic to create a style component like this. But you can use this method to add a CSS to your website. Here is an example:

```py linenums="1" title="Example of Style component" hl_lines="5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 34"
from fronty.css import CSS, Selector
from fronty.html import Html, Head, Title, Meta, Style, Body, H1

css = CSS(
    Selector('body')
    .properties({
        "background-color": "red",
        "color": "white",
        "font-size": "20px",
        "font-weight": "bold",
        "padding": "10px",
        "border-radius": "5px",
        "border": "1px solid black"
    }),
    Selector('h1')
    .properties({
        "color": "blue",
        "font-size": "30px",
        "font-weight": "bold",
        "padding": "10px",
        "border-radius": "5px",
        "border": "1px solid black"
    }),
)

...
# Now we will add the style component to the html component

html = Html(
    Head(
        Title('My Website'),
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Style(css.render())
    ),
    Body(
        H1('Hello World')
    )
)

print(html.render())
```

Output:

```html linenums="1" title="Output of the above code"
<!DOCTYPE html><html><head><title>My Website</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><style type="text/css" href="" rel="stylesheet">body{background-color:red;color:white;font-size:20px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}h1{color:blue;font-size:30px;font-weight:bold;padding:10px;border-radius:5px;border:1px solid black}</style></head><body><h1>Hello World</h1></body></html>
```

This is how you can add a CSS to your website fast, easily and efficiently with `Style` component.
