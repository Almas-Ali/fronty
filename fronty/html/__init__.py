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
