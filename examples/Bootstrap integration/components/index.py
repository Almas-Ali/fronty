from fronty.html import Element, Text, Break

# components
from components.layout import layout


def home(request, **data) -> Element:

    _layout = layout(
        request=request,
        content=Element(
            'div',
            Element('h1', 'Home'),

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


def about(request, **data) -> Element:

    _layout = layout(
        request=request,
        content=Element(
            'div',
            Element('h1', 'About'),
        ).class_('container text-center')
    )

    return _layout
