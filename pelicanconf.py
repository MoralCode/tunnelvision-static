AUTHOR = "Adrian Edwards"
SITENAME = "tunnelvision-static"
SITEURL = ""

PATH = "content"
THEME = "theme"
OUTPUT_PATH="output"

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'
STATIC_PATHS = ["images", "js"]


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARCHIVES_SAVE_AS = "catalog.html"
ARTICLE_SAVE_AS = 'catalog/{id}.html'

THEME_STATIC_DIR = "static"

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


IMAGE_PROCESS = {
    "article-image": ["scale_in 300 300 False"],
    "thumb": ["scale_in 180 180 False"],
}
IMAGE_PROCESS_DIR = "derived"
