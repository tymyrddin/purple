# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Laws of the forest'
copyright = '2022, Ty Myrddin'
author = 'Ty Myrddin'
release = '0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_markdown_tables',
    'sphinx.ext.intersphinx',
]

source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

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
    "red": ("https://red.tymyrddin.dev/en/latest", None),
    "red-app": ("https://red.tymyrddin.dev/projects/app/en/latest/", None),
    "red-recon": ("https://red.tymyrddin.dev/projects/recon/en/latest/", None),
    "red-enum": ("https://red.tymyrddin.dev/projects/enum/en/latest/", None),
    "red-acorns": ("https://red.tymyrddin.dev/projects/acorns/en/latest/", None),
    "red-iac": ("https://red.tymyrddin.dev/projects/iac/en/latest/", None),
    "red-hurdles": ("https://red.tymyrddin.dev/projects/fire/en/latest/", None),
    "red-ad": ("https://red.tymyrddin.dev/projects/ad/en/latest/", None),
    "red-api": ("https://red.tymyrddin.dev/projects/api/en/latest/", None),
    "red-escalation": ("https://red.tymyrddin.dev/projects/escalation/en/latest/", None),
    "red-network": ("https://red.tymyrddin.dev/projects/network/en/latest/", None),
    "red-crypt": ("https://red.tymyrddin.dev/projects/crypto/en/latest/", None),
    "red-cloud": ("https://red.tymyrddin.dev/projects/cloud/en/latest/", None),
    "red-bbh": ("https://red.tymyrddin.dev/projects/bbh/en/latest/", None),
    "blue": ("https://blue.tymyrddin.dev/en/latest", None),
    "green": ("https://green.tymyrddin.dev/en/latest", None),
    "green-soup": ("https://green.tymyrddin.dev/projects/soup/en/latest/", None),
}

myst_url_schemes = ["http", "https", ]
