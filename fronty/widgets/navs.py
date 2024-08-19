from typing import Self

from fronty import html
from fronty import css
from fronty.widgets import BaseWidget


class NavsWidget(BaseWidget):
    '''This is the navigation bar widget.'''

    def __init__(self, load_css: bool = False, *args, **kwargs) -> None:
        super().__init__(load_css=load_css, *args, **kwargs)

        self.__elements: list[html.Anchor] = []

    def add_element(self, element: html.Element, first: bool = False) -> Self:
        '''Adds an element to the widget.'''

        if first is True:
            self.__elements.insert(0, element)
        else:
            self.__elements.append(element)

        return self

    def add_nav_link(self, text: str, href: str, *attrs) -> Self:
        '''
        Adds a navigation link to the navigation bar.

        Args:
            text (str): The text of the link.
            href (str): The href of the link.
            *attrs (key, value): Additional attributes.
        '''

        __element = html.Anchor(text, href=href).class_('nav-link')
        for key, value in attrs:
            __element.attr(key, value)

        self.add_element(__element)

        return self

    def add_style_last_element(self, **styles) -> Self:
        '''
        Adds a style to the last element of the navigation bar.

        Args:
            **styles (key, value): The style of the last element.
        '''

        self.__elements[-1].style(**styles)

        return self

    def __style(self) -> css.CSS:
        '''This is the style of the page.'''

        return css.CSS(
            css.Selector('body').properties({
                'font-family': 'Noto Sans',
                'margin': '0',
                'padding': '0',
            }),
            css.Selector('.navbar').properties({
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
                'background-color': '#f1f1f1',
                'padding': '10px',
                'margin-bottom': '10px',
            }),
            css.Selector('.nav-link').properties({
                'text-decoration': 'none',
            }),
            css.Selector('.nav-link:hover').properties({
                'text-decoration': 'overline',
                'text-decoration-thickness': '2px',
            }),
        )

    def render(self) -> str:
        '''Renders the widget.'''

        return html.Section(
            html.Style(
                self.__style()
            ) if self.load_css is True else html.Style(),

            html.Nav(
                *self.__elements
            )
            .class_('navbar')
            .id('navbar')
        ).render()
