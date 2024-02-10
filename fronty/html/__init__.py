from typing import Union


class BaseElement:
    '''Base element.'''

    def __init__(self, tag, *children, **attributes):
        self.tag = tag
        self.children = list(children)
        self.attributes = dict(attributes)

    def __str__(self):
        return self.render()

    def render(self):
        '''
        Renders the element.
        Example:
            Element().render()

        Returns:
            str: The element.

        Output:
            <tag any="any" attribute="attribute">children</tag>
        '''

        # Check if the element is empty
        _is_space: str = ' ' if self._render_attributes() else ''

        return f'<{self.tag}{_is_space}{self._render_attributes()}>{self._render_children()}</{self.tag}>'

    def _render_attributes(self):
        '''
        Renders the attributes of the element.
        Example:
            Element()._render_attributes()

        Returns:
            str: The attributes of the element.

        Output:
            <tag any="any" attribute="attribute"></tag>
        '''

        return ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())

    def _render_children(self):
        '''
        Renders the children of the element.
        Example:
            Element()._render_children()

        Returns:
            str: The children of the element.

        Output:
            <tag>children</tag>
        '''

        return ''.join(str(child) for child in self.children)

    def style(self, **kwargs):
        '''
        Sets the style of the element.
        Example:
            Element().style(color='red', background='black')

        Returns:
            Element: The element with the style set.

        Output:
            <tag style="color: red; background: black;"></tag>
        '''
        modified_kwargs = {}
        for key, value in kwargs.items():
            modified_key = key.replace('_', '-')
            modified_kwargs[modified_key] = value

        kwargs = modified_kwargs

        self.attributes['style'] = ';'.join(
            f'{key}:{value}' for key, value in kwargs.items()
        ) + ';'

        return self

    def class_(self, *args):
        '''
        Sets the class of the element.
        Example:
            Element().class_('class1', 'class2', 'classNth')

        Returns:
            Element: The element with the class set.

        Output:
            <tag class="class1 class2 classNth"></tag>
        '''

        self.attributes['class'] = ' '.join(args)
        return self

    def id(self, id):
        '''
        Sets the id of the element.
        Example:
            Element().id('id')

        Returns:
            Element: The element with the id set.

        Output:
            <tag id="id"></tag>
        '''

        self.attributes['id'] = id
        return self

    def attr(self, key, value):
        '''
        Sets the attribute of the element.
        Example:
            Element().attr('name', 'value')

        Returns:
            Element: The element with the attribute set.

        Output:
            <tag name="value"></tag>
        '''

        self.attributes[key] = value
        return self

    @property
    def required(self):
        '''
        Sets the required attribute of the element.
        Example:
            Element().required

        Returns:
            Element: The element with the required attribute set.

        Output:
            <tag required></tag>
        '''

        self.attributes['required'] = ''
        return self

    @property
    def disabled(self):
        '''
        Sets the disabled attribute of the element.
        Example:
            Element().disabled

        Returns:
            Element: The element with the disabled attribute set.

        Output:
            <tag disabled></tag>
        '''

        self.attributes['disabled'] = ''
        return self

    @property
    def readonly(self):
        '''
        Sets the readonly attribute of the element.
        Example:
            Element().readonly

        Returns:
            Element: The element with the readonly attribute set.

        Output:
            <tag readonly></tag>
        '''

        self.attributes['readonly'] = ''
        return self

    def value(self, value):
        '''
        Sets the value attribute of the element.
        Example:
            Element().value('value')

        Returns:
            Element: The element with the value attribute set.

        Output:
            <tag value="value"></tag>
        '''

        self.attributes['value'] = value
        return self

    def placeholder(self, placeholder):
        '''
        Sets the placeholder attribute of the element.
        Example:
            Element().placeholder('placeholder')

        Returns:
            Element: The element with the placeholder attribute set.

        Output:
            <tag placeholder="placeholder"></tag>
        '''

        self.attributes['placeholder'] = placeholder
        return self

    def type(self, type):
        '''
        Sets the type attribute of the element.
        Example:
            Element().type('type')

        Returns:
            Element: The element with the type attribute set.

        Output:
            <tag type="type"></tag>
        '''

        self.attributes['type'] = type
        return self

    def name(self, name):
        '''
        Sets the name attribute of the element.
        Example:
            Element().name('name')

        Returns:
            Element: The element with the name attribute set.

        Output:
            <tag name="name"></tag>
        '''

        self.attributes['name'] = name
        return self

    def __repr__(self):
        return f'<{self.tag} {self.attributes}>'

    def __call__(self):
        return self

    def __add__(self, other):
        return self.children.append(other)


class Html(BaseElement):
    '''Html element.'''

    def __init__(self, *children, **attributes):
        super().__init__('html', *children, **attributes)

    def render(self):
        return f'<!DOCTYPE html>{super().render()}'


class Head(BaseElement):
    '''Head element.'''

    def __init__(self, *children, **attributes):
        super().__init__('head', *children, **attributes)

    def title(self, title):
        self.children.append(Title(title))
        return self

    def meta(self, **kwargs):
        self.children.append(Meta(**kwargs))
        return self

    def link(self, **kwargs):
        self.children.append(Link(**kwargs))
        return self

    def script(self, **kwargs):
        self.children.append(Script(**kwargs))
        return self

    def style(self, **kwargs):
        self.children.append(Style(**kwargs))
        return self

    def __add__(self, other):
        self.children.append(other)
        return self


class Title(BaseElement):
    '''Title element.'''''

    def __init__(self, *children, **attributes):
        super().__init__('title', *children, **attributes)


class Script(BaseElement):
    '''Script element.'''

    def __init__(self, *children, **attributes):
        super().__init__('script', *children, **attributes)
        self.attributes['type'] = 'text/javascript' if 'type' not in attributes else attributes['type']
        self.attributes['src'] = attributes['src'] if 'src' in attributes else ''


class Style(BaseElement):
    '''Style element.'''

    def __init__(self, *children, **attributes):
        super().__init__('style', *children, **attributes)
        self.attributes['type'] = 'text/css' if 'type' not in attributes else attributes['type']
        self.attributes['href'] = attributes['href'] if 'href' in attributes else ''
        self.attributes['rel'] = 'stylesheet' if 'rel' not in attributes else attributes['rel']

    def render(self):
        '''render all inner css.Selector elements'''
        _styles = ''.join(child.render() for child in self.children)
        _is_space = ' ' if self._render_attributes() else ''
        return f'<{self.tag}{_is_space}{self._render_attributes()}>{_styles}</{self.tag}>'


class Body(BaseElement):
    '''Body element.'''

    def __init__(self, *children, **attributes):
        super().__init__('body', *children, **attributes)

    def __add__(self, other):
        self.children.append(other)
        return self


class Meta(BaseElement):
    '''Meta element.'''

    def __init__(self, **attributes):
        super().__init__('meta', **attributes)

    def render(self):
        _is_space = ' ' if self._render_attributes() else ''
        return f'<{self.tag}{_is_space}{self._render_attributes()}>'


class Element(BaseElement):
    '''Element element.'''

    def __init__(self, tag, *children, **attributes):
        super().__init__(tag, *children, **attributes)


class Link(BaseElement):
    '''Link element.'''

    def __init__(self, href, *children, **attributes):
        super().__init__('link', *children, **attributes)
        self.attributes['type'] = 'text/css' if 'type' not in attributes else attributes['type']
        self.attributes['rel'] = 'stylesheet' if 'rel' not in attributes else attributes['rel']
        self.attributes['href'] = href

    def render(self):
        _is_space = ' ' if self._render_attributes() else ''
        return f'<{self.tag}{_is_space}{self._render_attributes()}>'


class Anchor(BaseElement):
    '''Anchor element.'''

    def __init__(self, *children, **attributes):
        super().__init__('a', *children, **attributes)


class Image(BaseElement):
    '''Image element.'''

    def __init__(self, src, *children, **attributes):
        super().__init__('img', *children, **attributes)
        self.attributes['src'] = src

    def render(self):
        _is_space = ' ' if self._render_attributes() else ''
        return f'<{self.tag}{_is_space}{self._render_attributes()}>'


class Button(BaseElement):
    '''Button element.'''

    def __init__(self, *children, **attributes):
        super().__init__('button', *children, **attributes)
        self.attributes['type'] = 'button'


class Input(BaseElement):
    '''Input element.'''

    def __init__(self, *children, **attributes):
        super().__init__('input', *children, **attributes)
        self.attributes['type'] = 'text' if 'type' not in attributes else attributes['type']

    def render(self):
        _is_space = ' ' if self._render_attributes() else ''
        return f'<{self.tag}{_is_space}{self._render_attributes()}>'

    def _render_attributes(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())

    def _render_children(self):
        return ''


class Text(BaseElement):
    '''Text element.'''

    def __init__(self, *children, **attributes):
        super().__init__('p', *children, **attributes)


class Break(BaseElement):
    '''Break element.'''

    def __init__(self, *children, **attributes):
        super().__init__('br', *children, **attributes)

    def render(self):
        return '<br>'


class Form(BaseElement):
    '''Form element.'''

    def __init__(self, *children, **attributes):
        super().__init__('form', *children, **attributes)

    def method(self, method):
        self.attributes['method'] = method
        return self

    def action(self, action):
        self.attributes['action'] = action
        return self

    def enctype(self, enctype):
        self.attributes['enctype'] = enctype
        return self


class Label(BaseElement):
    '''Label element.'''

    def __init__(self, *children, **attributes):
        super().__init__('label', *children, **attributes)
        self.attributes['for'] = attributes['for'] if 'for' in attributes else ''


class Select(BaseElement):
    '''Select element.'''

    def __init__(self, *children, **attributes):
        super().__init__('select', *children, **attributes)


class Option(BaseElement):
    '''Option element.'''

    def __init__(self, *children, **attributes):
        super().__init__('option', *children, **attributes)
        self.attributes['value'] = attributes['value'] if 'value' in attributes else ''


class Table(BaseElement):
    '''Table element.'''

    def __init__(self, *children, **attributes):
        super().__init__('table', *children, **attributes)


class Thead(BaseElement):
    '''Thead element.'''

    def __init__(self, *children, **attributes):
        super().__init__('thead', *children, **attributes)


class Tbody(BaseElement):
    '''Tbody element.'''

    def __init__(self, *children, **attributes):
        super().__init__('tbody', *children, **attributes)


class Tr(BaseElement):
    '''Tr element.'''

    def __init__(self, *children, **attributes):
        super().__init__('tr', *children, **attributes)


class Th(BaseElement):
    '''Th element.'''

    def __init__(self, *children, **attributes):
        super().__init__('th', *children, **attributes)


class Td(BaseElement):
    '''Td element.'''

    def __init__(self, *children, **attributes):
        super().__init__('td', *children, **attributes)


class H1(BaseElement):
    '''H1 element.'''

    def __init__(self, *children, **attributes):
        super().__init__('h1', *children, **attributes)


class H2(BaseElement):
    '''H2 element.'''

    def __init__(self, *children, **attributes):
        super().__init__('h2', *children, **attributes)


class H3(BaseElement):
    '''H3 element.'''

    def __init__(self, *children, **attributes):
        super().__init__('h3', *children, **attributes)


class H4(BaseElement):
    '''H4 element.'''

    def __init__(self, *children, **attributes):
        super().__init__('h4', *children, **attributes)


class H5(BaseElement):
    '''H5 element.'''

    def __init__(self, *children, **attributes):
        super().__init__('h5', *children, **attributes)


class H6(BaseElement):
    '''H6 element.'''

    def __init__(self, *children, **attributes):
        super().__init__('h6', *children, **attributes)


class Ul(BaseElement):
    '''Ul element.'''

    def __init__(self, *children, **attributes):
        super().__init__('ul', *children, **attributes)


class Ol(BaseElement):
    '''Ol element.'''

    def __init__(self, *children, **attributes):
        super().__init__('ol', *children, **attributes)


class Li(BaseElement):
    '''Li element.'''

    def __init__(self, *children, **attributes):
        super().__init__('li', *children, **attributes)


class Span(BaseElement):
    '''Span element.'''

    def __init__(self, *children, **attributes):
        super().__init__('span', *children, **attributes)


class Div(BaseElement):
    '''Div element.'''

    def __init__(self, *children, **attributes):
        super().__init__('div', *children, **attributes)


class Nav(BaseElement):
    '''Nav element.'''

    def __init__(self, *children, **attributes):
        super().__init__('nav', *children, **attributes)


class Footer(BaseElement):
    '''Footer element.'''

    def __init__(self, *children, **attributes):
        super().__init__('footer', *children, **attributes)


class Header(BaseElement):
    '''Header element.'''

    def __init__(self, *children, **attributes):
        super().__init__('header', *children, **attributes)


class Section(BaseElement):
    '''Section element.'''

    def __init__(self, *children, **attributes):
        super().__init__('section', *children, **attributes)


class Article(BaseElement):
    '''Article element.'''

    def __init__(self, *children, **attributes):
        super().__init__('article', *children, **attributes)


class Aside(BaseElement):
    '''Aside element.'''

    def __init__(self, *children, **attributes):
        super().__init__('aside', *children, **attributes)


class Main(BaseElement):
    '''Main element.'''

    def __init__(self, *children, **attributes):
        super().__init__('main', *children, **attributes)


class Figure(BaseElement):
    '''Figure element.'''

    def __init__(self, *children, **attributes):
        super().__init__('figure', *children, **attributes)


class Figcaption(BaseElement):
    '''Figcaption element.'''

    def __init__(self, *children, **attributes):
        super().__init__('figcaption', *children, **attributes)


class Dl(BaseElement):
    '''Dl element.'''

    def __init__(self, *children, **attributes):
        super().__init__('dl', *children, **attributes)


class Dt(BaseElement):
    '''Dt element.'''

    def __init__(self, *children, **attributes):
        super().__init__('dt', *children, **attributes)


class Dd(BaseElement):
    '''Dd element.'''

    def __init__(self, *children, **attributes):
        super().__init__('dd', *children, **attributes)


class Small(BaseElement):
    '''Small element.'''

    def __init__(self, *children, **attributes):
        super().__init__('small', *children, **attributes)


class Time(BaseElement):
    '''Time element.'''

    def __init__(self, *children, **attributes):
        super().__init__('time', *children, **attributes)


class Strong(BaseElement):
    '''Strong element.'''

    def __init__(self, *children, **attributes):
        super().__init__('strong', *children, **attributes)


class Em(BaseElement):
    '''Emphasis element.'''

    def __init__(self, *children, **attributes):
        super().__init__('em', *children, **attributes)


class Mark(BaseElement):
    '''Mark element.'''

    def __init__(self, *children, **attributes):
        super().__init__('mark', *children, **attributes)


class Code(BaseElement):
    '''Code element.'''

    def __init__(self, *children, **attributes):
        super().__init__('code', *children, **attributes)


class Pre(BaseElement):
    '''Pre element.'''

    def __init__(self, *children, **attributes):
        super().__init__('pre', *children, **attributes)


class Blockquote(BaseElement):
    '''Blockquote element.'''

    def __init__(self, *children, **attributes):
        super().__init__('blockquote', *children, **attributes)


class Iframe(BaseElement):
    '''Iframe element.'''

    def __init__(self, *children, **attributes):
        super().__init__('iframe', *children, **attributes)


class Video(BaseElement):
    '''Video element.'''

    def __init__(self, *children, **attributes):
        super().__init__('video', *children, **attributes)


class Audio(BaseElement):
    '''Audio element.'''

    def __init__(self, *children, **attributes):
        super().__init__('audio', *children, **attributes)


class Source(BaseElement):
    '''Source element for video and audio.'''

    def __init__(self, *children, **attributes):
        super().__init__('source', *children, **attributes)


class I(BaseElement):
    '''I element.'''

    def __init__(self, *children, **attributes):
        super().__init__('i', *children, **attributes)


class Empty(BaseElement):
    '''Empty element.'''

    def __init__(self, *children, **attributes):
        super().__init__('', *children, **attributes)

    def render(self):
        return ''.join(str(child) for child in self.children)

    def _render_children(self):
        return ''.join(str(child) for child in self.children)

    def _render_attributes(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())

    def __add__(self, other):
        self.children.append(other)
        return self

    def __str__(self):
        return self.render()


AnyHTMLElement = Union[
    Html,
    Head,
    Title,
    Script,
    Style,
    Body,
    Meta,
    Link,
    Anchor,
    Image,
    Button,
    Input,
    Text,
    Break,
    Form,
    Label,
    Select,
    Option,
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Ul,
    Ol,
    Li,
    Span,
    Div,
    Nav,
    Footer,
    Header,
    Section,
    Article,
    Aside,
    Main,
    Figure,
    Figcaption,
    Dl,
    Dt,
    Dd,
    Small,
    Time,
    Strong,
    Em,
    Mark,
    Code,
    Pre,
    Blockquote,
    Iframe,
    Video,
    Audio,
    Source,
    I,
    Empty,
]
