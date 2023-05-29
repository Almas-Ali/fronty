'''
All types of HTML widgets are defined here.
'''

from fronty import html
from fronty import css

# Work in progress. Not ready yet.


class BaseWidget(html.BaseElement):
    '''This is the base class for all widgets.'''

    def __init__(self, *args, **kwargs):
        super().__init__(tag='', *args, **kwargs)
        self._element: dict = {}

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


class FormWidget(BaseWidget):
    '''This is the base class for all form widgets.'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.forms_type = [
            'loginform',
            'registrationform',
            'contactform',
            'searchform',
            'subscribeform',
            'commentform',
        ]
        self._type = self.forms_type[0]
        self._action = kwargs['action'] if 'action' in kwargs else '#'
        self._method = kwargs['method'] if 'method' in kwargs else 'post'
        self.load_css = True if 'load_css' in kwargs else False

    def render(self):
        '''Renders the widget.'''
        if self._type in self.forms_type:
            return self.__get_form().render()

    def __get_form(self):
        '''Generates the form.'''
        if self._type == 'loginform':
            return self.__get_loginform()
        elif self._type == 'registrationform':
            return self.__get_registrationform()
        elif self._type == 'contactform':
            return self.__get_contactform()
        elif self._type == 'searchform':
            return self.__get_searchform()
        elif self._type == 'subscribeform':
            return self.__get_subscribeform()
        elif self._type == 'commentform':
            return self.__get_commentform()

    def __get_loginform(self):
        '''Login form.'''

        # All login styles are here.
        styles = css.CSS(
            css.Selector('#form-object').properties({
                'font-family': 'Arial, Helvetica, sans-serif'
            }),
            css.Selector('form').properties({
                'border': '3px solid #f1f1f1',
                'padding': '10px',
            }),
            css.Selector('.form-tags').properties({
                'display': 'flex',
                'flex-direction': 'column',
                'justif-items': 'center'
            }),
            css.Selector('button').properties({
                'background-color': '#04AA6D',
                'color': 'white',
                'padding': '14px 20px',
                'margin': '8px 0',
                'border': 'none',
                'cursor': 'pointer',
                'width': '100%',
            }),
            css.Selector('button:hover').properties({
                'opacity': '0.8'
            }),
            css.Selector('input[type=text], input[type=password]').properties({
                'width': '100%',
                'padding': '12px 20px',
                'margin': '8px 0',
                'display': 'inline-block',
                'border': '1px solid #ccc',
                'box-sizing': 'border-box',
            }),
        )

        # This returns a HTML section tag that contains the form.
        return html.Section(

            # All styles are included here if load_css is True.
            html.Style(
                styles.render()
            ) if self.load_css is True else html.Style(),

            html.Form(
                self._element.get('first') if 'first' in self._element else '',
                html.Div(
                    html.Label('Username'),
                    html.Input(type='text', name='username',
                               placeholder='Username'),
                ),
                html.Div(
                    html.Label('Password'),
                    html.Input()
                    .type('password')
                    .name('password')
                    .placeholder('********')
                ),
                html.Div(
                    html.Button('Submit')
                    .type('submit'),
                ),
                self._element.get('last') if 'last' in self._element else '',
            )
            .attr('action', self._action)
            .attr('method', self._method)
            .id('form-object'),
        )

    def __get_registrationform(self):
        '''Register form'''
        styles = css.CSS(
            css.Selector('#form-object').properties({
                'font-family': 'Arial, Helvetica, sans-serif'
            }),
            css.Selector('form').properties({
                'border': '3px solid #f1f1f1',
                'padding': '10px',
            }),
            css.Selector('.form-tags').properties({
                'display': 'flex',
                'flex-direction': 'column',
                'justif-items': 'center'
            }),
            css.Selector('button').properties({
                'background-color': '#04AA6D',
                'color': 'white',
                'padding': '14px 20px',
                'margin': '8px 0',
                'border': 'none',
                'cursor': 'pointer',
                'width': '100%',
            }),
            css.Selector('button:hover').properties({
                'opacity': '0.8'
            }),
            css.Selector('input[type=text], input[type=password]').properties({
                'width': '100%',
                'padding': '12px 20px',
                'margin': '8px 0',
                'display': 'inline-block',
                'border': '1px solid #ccc',
                'box-sizing': 'border-box',
            }),
        )

        return html.Section(

            html.Style(
                styles.render()
            ) if self.load_css is True else html.Style(),

            html.Form(
                self._element.get('first') if 'first' in self._element else '',

                html.Div(
                    html.Label('Username'),
                    html.Input(type='text', name='username',
                               placeholder='Username'),
                ),
                html.Div(
                    html.Label('Password'),
                    html.Input(type='password', name='password', placeholder='****'
                               ),
                    html.Div(
                        html.Button('Submit', type='submit'),
                    ),
                ),

                self._element.get('last') if 'last' in self._element else '',
            ).id('form-object'),
        )
