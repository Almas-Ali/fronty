from ..html import AnyHTMLElement


class BaseElement(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def render(self):
        raise NotImplementedError

    def script_wrap(self):
        '''Returns the JS code wrapped in <script> tags.'''
        return f"<script>{self.render()}</script>"

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.render()

    def __add__(self, other):
        return self.render() + other.render()

    def __radd__(self, other):
        return other.render() + self.render()

    def __iadd__(self, other):
        return self.render() + other.render()

    def __eq__(self, other):
        return self.render() == other.render()

    def __ne__(self, other):
        return self.render() != other.render()

    def __lt__(self, other):
        return self.render() < other.render()

    def __le__(self, other):
        return self.render() <= other.render()

    def __gt__(self, other):
        return self.render() > other.render()

    def __ge__(self, other):
        return self.render() >= other.render()

    def __len__(self):
        return len(self.render())


class Alert(BaseElement):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def render(self):
        return f"alert('{self.message}');"


class Event(BaseElement):
    def __init__(self, event, **kwargs):
        super().__init__(**kwargs)
        self.event = event

    def render(self):
        return f"document.getElementById('{self.kwargs.get('id')}').{self.event}();" if 'id' in self.kwargs else f"document.{self.event}();"


class ConsoleLog(BaseElement):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def render(self):
        return f"console.log('{self.message}');"


class Function(BaseElement):
    def __init__(self, name, args: list, body: str):
        super().__init__()
        self.name = name
        self.args = args
        self.body = body

    def render(self):
        return f"function {self.name}({', '.join(self.args)}){{ {self.body} }};"


class SetTimeout(BaseElement):
    def __init__(self, function, time):
        super().__init__()
        self.function = function
        self.time = time

    def render(self):
        return f"setTimeout({self.function}, {self.time});"


class SetInterval(BaseElement):
    def __init__(self, function, time: int):
        super().__init__()
        self.function = function
        self.time = time

    def render(self):
        return f"setInterval({self.function}, {self.time});"


class ToggleClass(BaseElement):
    def __init__(self, html: AnyHTMLElement, class1: str, class2: str):
        super().__init__()
        self.html = html
        self.class1 = class1
        self.class2 = class2

    def render(self):
        return self.html.class_
