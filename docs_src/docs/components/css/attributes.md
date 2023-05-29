# Attributes of CSS Components

## Attributes

### properties

`properties` is a dictionary that contains all the properties of a CSS component. It is a required attribute of a `Selector` element. You have to pass a dictionary to this attribute. The keys of the dictionary are the properties of the CSS component and the values of the dictionary are the values of the properties. Here is an example:

```python linenums="1" title="Example of properties attribute" hl_lines="5 6 7 8 9 10 11 12 13"
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

***Fronty returns every frontend code minified for better performance.***

