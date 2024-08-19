'''
The base module for all widgets in Fronty.
'''

from fronty import html
from fronty import css


class BaseWidget(html.BaseElement):
    '''This is the base class for all widgets.'''

    def __init__(self, load_css: bool = False, *args, **kwargs):
        super().__init__(tag='', *args, **kwargs)
        self._element: dict = {}
        self.load_css = load_css

    def add_element(self, element: html.Element, first=False):
        '''Adds an element to the widget.'''
        if first is True:
            self._element['first'] = element.render()
        else:
            self._element['last'] = element.render()

        return self

    def remove_element(self, element):
        '''Removes an element from the widget.'''
        self._element.pop(element)
        return self

    def select_element(self, name: str = None, id: str = None, class_: str = None, index: int = None):
        '''Selects an element from the widget.'''
        if name is not None:
            return self._element[name]
        elif id is not None:
            return self._element[id]
        elif class_ is not None:
            return self._element[class_]
        elif index is not None:
            return self._element[index]
        else:
            return self._element

    def __attr__(self, key, value):
        self.attributes[key] = value
        return self

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()

    def render(self) -> str:
        '''Renders the widget.'''
        return self._element['first'] + self._element['last']
