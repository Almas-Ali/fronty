from fronty import html
from fronty import css
from fronty.widgets import BaseWidget


class FormWidget(BaseWidget):
    '''This is the base class for all form widgets.'''

    def __init__(
        self,
        load_css: bool = False,
        action: str = '#',
        method: str = 'get',
        *args,
        **kwargs
    ) -> None:
        super().__init__(load_css=load_css, *args, **kwargs)

        # Form attributes
        self.action = action
        self.method = method
        self.styles = css.CSS(
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

    def _create_form(self, *data) -> html.Section:
        '''Creates the form.'''

        return html.Section(

            html.Style(
                self.styles
            ) if self.load_css is True else html.Style(),

            html.Form(
                self._element.get('first') if 'first' in self._element else '',
                *data,
                self._element.get('last') if 'last' in self._element else '',
            )
            .attr('action', self.action)
            .attr('method', self.method)
            .id('form-object'),
        ).render()


class RegistrationForm(FormWidget):
    '''This is the registration form.'''

    def render(self) -> html.Section:
        '''Renders the registration form.'''

        return self._create_form(
            html.Div(
                html.Label('First Name'),
                html.Input(type='text', name='first-name',
                           placeholder='First Name'),
            ),

            html.Div(
                html.Label('Last Name'),
                html.Input(type='text', name='last-name',
                           placeholder='Last Name'),
            ),

            html.Div(
                html.Label('Email'),
                html.Input(type='text', name='email',
                           placeholder='Email'),
            ),

            html.Div(
                html.Label('Username'),
                html.Input(type='text', name='username',
                           placeholder='Username'),
            ),
            html.Div(
                html.Label('Password'),
                html.Input(type='password', name='password',
                           placeholder='*'*8),
            ),
            html.Div(
                html.Label('Confirm Password'),
                html.Input(type='password',
                           name='confirm-password', placeholder='*'*8),
            ),
            html.Div(
                html.Button('Submit', type='submit'),
            ),
        )


class LoginForm(FormWidget):
    '''This is the login form.'''

    def render(self) -> html.Section:
        '''Renders the login form.'''

        return self._create_form(
            html.Div(
                html.Label('Username'),
                html.Input(type='text', name='username',
                           placeholder='Username'),
            ),

            html.Div(
                html.Label('Password'),
                html.Input(type='password', name='password',
                           placeholder='*'*8),
            ),
            html.Div(
                html.Button('Submit', type='submit'),
            ),
        )


class ContactForm(FormWidget):
    '''This is the contact form.'''

    def render(self) -> html.Section:
        '''Renders the contact form.'''

        return self._create_form(
            html.Div(
                html.Label('Full Name'),
                html.Input(type='text', name='full-name',
                           placeholder='Full Name'),
            ),

            html.Div(
                html.Label('Email'),
                html.Input(type='text', name='email',
                           placeholder='Email'),
            ),

            html.Div(
                html.Label('Message'),
                html.Break(),
                html.Textarea(
                    col=30,
                    row=10,
                    name='message',
                    placeholder='Type your message here...',
                )
            ),
            html.Div(
                html.Button('Submit', type='submit'),
            ),
        )


class SearchForm(FormWidget):
    '''This is the search form.'''

    def render(self) -> html.Section:
        '''Renders the search form.'''

        return self._create_form(
            html.Div(
                html.Label('Search'),
                html.Input(type='text', name='search',
                           placeholder='Search...'),
            ),
            html.Div(
                html.Button('Submit', type='submit'),
            ),
        )


class SubscribeForm(FormWidget):
    '''This is the subscription form.'''

    def render(self) -> html.Section:
        '''Renders the subscription form.'''

        return self._create_form(
            html.Div(
                html.Label('Email'),
                html.Input(type='text', name='email',
                           placeholder='Email'),
            ),
            html.Div(
                html.Button('Submit', type='submit'),
            ),
        )
