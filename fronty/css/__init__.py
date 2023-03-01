class BaseCSS(object):
    def __init__(self, css):
        self.css = css

    def __str__(self):
        return '<BaseCSS Object>'

    def __add__(self, other):
        return BaseCSS(self.css + other.css)

    def __radd__(self, other):
        return BaseCSS(other.css + self.css)

    def __repr__(self):
        return f'<BaseCSS {self.css}>'

    def __call__(self):
        return self

    def __eq__(self, other):
        return self.css == other.css

    def __ne__(self, other):
        return self.css != other.css

    def __lt__(self, other):
        return self.css < other.css

    def __le__(self, other):
        return self.css <= other.css

    def __gt__(self, other):
        return self.css > other.css

    def __ge__(self, other):
        return self.css >= other.css

    def __hash__(self):
        return hash(self.css)

    def __len__(self):
        return len(self.css)

    def __getitem__(self, key):
        return self.css[key]

    def __setitem__(self, key, value):
        self.css[key] = value

    def __delitem__(self, key):
        del self.css[key]

    def __iter__(self):
        return iter(self.css)

    def __reversed__(self):
        return reversed(self.css)

    def __contains__(self, item):
        return item in self.css

    def __missing__(self, key):
        return self.css[key]

    def render(self):
        return self.css


class CSS(BaseCSS):
    def __init__(self, *selectors):
        self.selectors = list(selectors)
        super().__init__(''.join(str(selector) for selector in self.selectors))

    def __str__(self):
        return '<CSS Object>'

    def __add__(self, other):
        return CSS(*self.selectors, *other.selectors)

    def __radd__(self, other):
        return CSS(*other.selectors, *self.selectors)

    def __repr__(self):
        return f'<CSS {self.selectors}>'

    def __call__(self):
        return self

    def __eq__(self, other):
        return self.selectors == other.selectors

    def __ne__(self, other):
        return self.selectors != other.selectors

    def __lt__(self, other):
        return self.selectors < other.selectors

    def __le__(self, other):
        return self.selectors <= other.selectors

    def __gt__(self, other):
        return self.selectors > other.selectors

    def __ge__(self, other):
        return self.selectors >= other.selectors

    def __hash__(self):
        return hash(self.selectors)

    def __len__(self):
        return len(self.selectors)

    def __getitem__(self, key):
        return self.selectors[key]

    def __setitem__(self, key, value):
        self.selectors[key] = value

    def __delitem__(self, key):
        del self.selectors[key]

    def __iter__(self):
        return iter(self.selectors)

    def __reversed__(self):
        return reversed(self.selectors)

    def __contains__(self, item):
        return item in self.selectors

    def __missing__(self, key):
        return self.selectors[key]

    def render(self):
        return ''.join(selector.render() for selector in self.selectors)


class Selector(BaseCSS):
    def __init__(self, selector, *children, **attributes):
        self.selector = selector
        self.children = list(children)
        self.attributes = dict(attributes)
        super().__init__(f'{self.selector} {{ {self.render_attributes()} }}')

    def render_attributes(self):
        return ';'.join(f'{key}:{value}' for key, value in self.attributes.items())

    def render(self):
        return f'{self.selector}{{{self.render_attributes()}}}'

    def __str__(self):
        return '<Selector Object>'

    def properties(self, property_dict):
        self.attributes.update(property_dict)
        return self
