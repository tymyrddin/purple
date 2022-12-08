# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Laws of the forest'
copyright = '2022, Ty Myrddin'
author = 'Ty Myrddin'
release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_markdown_tables',
]

source_suffix = ['.rst', '.md']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False
}

html_title = "Laws of the forest"
html_logo = "img/logo.png"
html_favicon = "img/favicon.ico"

# Add any paths that contain templates here, relative to this directory.

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = []

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Intersphinx
intersphinx_mapping = {
    "red": ("https://tymyrddin.github.io/red/", None),
    "red-app": ("https://tymyrddin.github.io/red-app/", None),
    "red-recon": ("https://tymyrddin.github.io/red-recon/", None),
    "red-enum": ("https://tymyrddin.github.io/red-enum/", None),
    "red-acorns": ("https://tymyrddin.github.io/red-acorns/", None),
    "red-iac": ("https://tymyrddin.github.io/red-iac/", None),
    "red-hurdles": ("https://tymyrddin.github.io/red-hurdles/", None),
    "red-ad": ("https://tymyrddin.github.io/red-ad/", None),
    "red-api": ("https://tymyrddin.github.io/red-api/", None),
    "red-escalation": ("https://tymyrddin.github.io/red-escalation/", None),
    "red-network": ("https://tymyrddin.github.io/red-network/", None),
    "red-crypt": ("https://tymyrddin.github.io/red-crypt/", None),
    "red-cloud": ("https://tymyrddin.github.io/red-cloud/", None),
    "blue": ("https://tymyrddin.github.io/blue/", None),
    "green": ("https://tymyrddin.github.io/green/", None),
    "green-soup": ("https://tymyrddin.github.io/green-soup/", None),
}

myst_url_schemes = ["http", "https", ]
intersphinx_disabled_domains = ['std']

# -- Options for EPUB output
epub_show_urls = 'footnote'
