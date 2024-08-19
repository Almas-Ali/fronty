from typing import Self

from fronty import html
from fronty import css


class BasicTemplate:
    '''This is the basic template of the page.'''

    def __init__(self, *data: html.Element) -> Self:
        self.data = data
        self.meta = [
            html.Meta(charset="utf-8"),
            html.Meta(name="viewport",
                      content="width=device-width, initial-scale=1"),
        ]
        self.page_title = 'Fronty widgets example'
        self.style = css.CSS(
            css.Selector('.container').properties({
                'margin': '0',
                'padding': '0',
            })
        )

    def add_meta(self, meta: html.Meta) -> Self:
        '''Adds a meta tag to the page.'''

        self.meta.append(meta)
        return self

    def add_title(self, title: str) -> Self:
        '''Adds a title to the page.'''

        self.page_title = title
        return self

    def add_style(self, style: css.CSS) -> Self:
        '''Adds a style to the page.'''

        self.style = style
        return self

    def render(self) -> html.Element:
        return html.Html(
            html.Head(
                *self.meta,
                html.Title(self.page_title),
                html.Style(
                    self.style,
                ),
            ),
            html.Body(
                html.Div(
                    *self.data,
                ).class_("container"),
            )
        ).render()

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()
