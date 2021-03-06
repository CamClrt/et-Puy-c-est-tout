import os

AUTHOR = 'Camille'
SITENAME = ''
SITEURL = 'https://www.et-puy-c-est-tout.fr'

PATH = 'content'

URL_PREFIX = 'et-Puy-c-est-tout/' if os.environ.get("DEPLOYED") else ""

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('Instagram', 'https://www.instagram.com/et_puy_c_est_tout/'),)

DEFAULT_PAGINATION = 5

THEME = 'themes/attila'

STATIC_PATHS = ['assets']

HEADER_COVER = '/assets/images/blog_cover.jpg'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

INDEX_SAVE_AS = 'blog.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = [
    ('Home', f'{URL_PREFIX}index.html'),
    ('About', f'{URL_PREFIX}about.html'),
    ('Adresses', 'https://goo.gl/maps/9Df1Wgm2xKMovF6p9'),
    ('Articles', f'{URL_PREFIX}blog.html'),
]
