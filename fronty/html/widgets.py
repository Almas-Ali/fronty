'''
All types of HTML widgets are defined here.
'''

from fronty.html import (
    BaseElement
)

# Work in progress. Not ready yet.
class BaseWidget(BaseElement):
    '''This is the base class for all widgets.'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

