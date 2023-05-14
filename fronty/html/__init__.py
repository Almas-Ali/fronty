class BaseElement:
    def __init__(self, tag, *children, **attributes):
        self.tag = tag
        self.children = list(children)
        self.attributes = dict(attributes)

    def __str__(self):
        return self.render()

    def render(self):
        _is_space = ' ' if self.render_attributes() else ''
        return f'<{self.tag}{_is_space}{self.render_attributes()}>{self.render_children()}</{self.tag}>'

    def render_attributes(self):
        return ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())

    def render_children(self):
        return ''.join(str(child) for child in self.children)

    def style(self, **kwargs):
        self.attributes['style'] = ';'.join(
            f'{key}: {value}' for key, value in kwargs.items())
        return self

    def class_(self, *args):
        self.attributes['class'] = ' '.join(args)
        return self

    def id(self, id):
        self.attributes['id'] = id
        return self

    def attr(self, key, value):
        self.attributes[key] = value
        return self

    def __repr__(self):
        return f'<{self.tag} {self.attributes}>'

    def __call__(self):
        return self

    def __add__(self, other):
        return self.children.append(other)


class Html(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('html', *children, **attributes)

    def render(self):
        return f'<!DOCTYPE html>{super().render()}'


class Head(BaseElement):
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
    def __init__(self, *children, **attributes):
        super().__init__('title', *children, **attributes)


class Script(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('script', *children, **attributes)
        self.attributes['type'] = 'text/javascript' if 'type' not in attributes else attributes['type']
        self.attributes['src'] = attributes['src'] if 'src' in attributes else ''


class Style(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('style', *children, **attributes)
        self.attributes['type'] = 'text/css' if 'type' not in attributes else attributes['type']
        self.attributes['href'] = attributes['href'] if 'href' in attributes else ''
        self.attributes['rel'] = 'stylesheet' if 'rel' not in attributes else attributes['rel']


class Body(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('body', *children, **attributes)

    def __add__(self, other):
        self.children.append(other)
        return self


class Meta(BaseElement):
    def __init__(self, **attributes):
        super().__init__('meta', **attributes)


class Element(BaseElement):
    def __init__(self, tag, *children, **attributes):
        super().__init__(tag, *children, **attributes)


class Link(BaseElement):
    def __init__(self, href, *children, **attributes):
        super().__init__('link', *children, **attributes)
        self.attributes['type'] = 'text/css' if 'type' not in attributes else attributes['type']
        self.attributes['rel'] = 'stylesheet' if 'rel' not in attributes else attributes['rel']
        self.attributes['href'] = href


class Anchor(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('a', *children, **attributes)


class Image(BaseElement):
    def __init__(self, src, *children, **attributes):
        super().__init__('img', *children, **attributes)
        self.attributes['src'] = src


class Button(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('button', *children, **attributes)
        self.attributes['type'] = 'button'


class Input(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('input', *children, **attributes)
        self.attributes['type'] = 'text' if 'type' not in attributes else attributes['type']


class Text(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('p', *children, **attributes)


class Break(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('br', *children, **attributes)

    def render(self):
        return '<br>'


class Form(BaseElement):
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
    def __init__(self, *children, **attributes):
        super().__init__('label', *children, **attributes)
        self.attributes['for'] = attributes['for'] if 'for' in attributes else ''


class Select(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('select', *children, **attributes)


class Option(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('option', *children, **attributes)
        self.attributes['value'] = attributes['value'] if 'value' in attributes else ''


class Table(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('table', *children, **attributes)


class Thead(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('thead', *children, **attributes)


class Tbody(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('tbody', *children, **attributes)


class Tr(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('tr', *children, **attributes)


class Th(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('th', *children, **attributes)


class Td(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('td', *children, **attributes)


class H1(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('h1', *children, **attributes)


class H2(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('h2', *children, **attributes)


class H3(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('h3', *children, **attributes)


class H4(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('h4', *children, **attributes)


class H5(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('h5', *children, **attributes)


class H6(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('h6', *children, **attributes)


class Ul(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('ul', *children, **attributes)


class Ol(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('ol', *children, **attributes)

    
class Li(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('li', *children, **attributes)

    
class Span(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('span', *children, **attributes)


class Div(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('div', *children, **attributes)

    
class Nav(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('nav', *children, **attributes)


class Footer(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('footer', *children, **attributes)


class Header(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('header', *children, **attributes)


class Section(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('section', *children, **attributes)


class Article(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('article', *children, **attributes)


class Aside(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('aside', *children, **attributes)


class Main(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('main', *children, **attributes)


class Figure(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('figure', *children, **attributes)


class Figcaption(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('figcaption', *children, **attributes)


class Dl(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('dl', *children, **attributes)


class Dt(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('dt', *children, **attributes)


class Dd(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('dd', *children, **attributes)


class Small(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('small', *children, **attributes)


class Time(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('time', *children, **attributes)


class Strong(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('strong', *children, **attributes)


class Em(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('em', *children, **attributes)


class Mark(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('mark', *children, **attributes)


class Code(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('code', *children, **attributes)


class Pre(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('pre', *children, **attributes)


class Blockquote(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('blockquote', *children, **attributes)

        
class Iframe(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('iframe', *children, **attributes)


class Video(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('video', *children, **attributes)


class Audio(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('audio', *children, **attributes)


class Source(BaseElement):
    def __init__(self, *children, **attributes):
        super().__init__('source', *children, **attributes)


