from fronty.html import *


def navbar(request, **data) -> Element:
    '''
    This is the navbar component from bootstrap 5.3 docs, Now converted to fronty.

<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar scroll</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarScroll">
      <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
    '''

    _layout = Element(
        'nav',
        Element(
            'div',
            Anchor(
                'Fronty',
                href='/',
            ).class_('navbar-brand'),
            Button(
                Element('span').class_('navbar-toggler-icon'),

            ).class_('navbar-toggler').attr('type', 'button').attr('data-bs-toggle', 'collapse').attr('data-bs-target', '#navbarScroll').attr('aria-controls', 'navbarScroll').attr('aria-expanded', 'false').attr('aria-label', 'Toggle navigation'),
            Element(
                'ul',
                Element(
                    'li',
                    Anchor(
                        'Home',
                        href='/',
                    ).class_('nav-link active').attr('aria-current', 'page'),
                ).class_('nav-item'),
                Element(
                    'li',
                    Anchor(
                        'About',
                        href='/about',
                    ).class_('nav-link'),
                ).class_('nav-item'),
                Element(
                    'li',
                    Anchor(
                        'More',
                        href='#',
                    ).class_('nav-link dropdown-toggle').attr('role', 'button').attr('data-bs-toggle', 'dropdown').attr('aria-expanded', 'false'),
                    Element(
                        'ul',
                        Element(
                            'li',
                            Anchor(
                                'Action',
                                href='#',
                            ).class_('dropdown-item'),
                        ),
                        Element(
                            'li',
                            Anchor(
                                'Another action',
                                href='#',
                            ).class_('dropdown-item'),
                        ),
                        Element(
                            'li',
                            Element('hr').class_('dropdown-divider'),
                        ),
                        Element(
                            'li',
                            Anchor(
                                'Something else here',
                                href='#',
                            ).class_('dropdown-item'),
                        ),
                    ).class_('dropdown-menu'),
                ).class_('nav-item dropdown'),
            ).class_('navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll').attr('style', '--bs-scroll-height: 100px;'),
            Form(
                Input(
                    placeholder='Search',
                    aria_label='Search',
                ).class_('form-control me-2').attr('type', 'search'),
                Button(
                    'Search',
                ).class_('btn btn-outline-success').attr('type', 'submit'),
            ).class_('d-flex').attr('role', 'search'),

        ).class_('container-fluid'),
    ).class_('navbar navbar-expand-lg bg-body-tertiary')

    return _layout


def layout(request, **data) -> Html:
    return Html(
        Head(
            Title('Fronty'),  # Page title
            Meta(charset='utf-8'),  # Character encoding
            # Responsive design
            Meta(name='viewport', content='width=device-width, initial-scale=1'),

            # Bootstrap CSS
            Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css',
                 integrity='sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD', crossorigin='anonymous'),
        ),

        Body(

            # Navbar
            navbar(request),

            # Main area of the page
            data.get('content', 'Empty content'),

            # Bootstrap JS
            Script(src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js", integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN', crossorigin='anonymous'),
        ),
    )
