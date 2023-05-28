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
        self._value = None

    def add_element(self, element):
        '''Adds an element to the widget.'''
        self.append(element)

    def remove_element(self, element):
        '''Removes an element from the widget.'''
        self.remove(element)

    def select_element(self, index):
        '''Selects an element from the widget.'''
        self.select(index)

    def update_value(self, value):
        '''Updates the value of the widget.'''
        self._value = value


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
        args = list(args)
        if kwargs['load_css'] is True:
            self.load_css = True
        else:
            self.load_css = False

    def render(self):
        '''Renders the widget.'''
        if self._type in self.forms_type:
            return self.__get_form()

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
                html.Div(
                    html.Label('Username'),
                    html.Input(type='text', name='username',
                               placeholder='Username'),
                ),
                html.Div(
                    html.Label('Password'),
                    html.Input(type='password', name='password', placeholder='****'
                               ),
                ),
                html.Div(
                    html.Button('Submit', type='submit'),
                ),
            ).id('form-object'),
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
            ).id('form-object'),
        )
