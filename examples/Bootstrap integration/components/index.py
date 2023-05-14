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
