# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#project = 'YOLOv6'
project = 'YOLOv6_docs'
copyright = '2022, meituan'
author = 'meituan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst-parser', 'sphinx_theme', 'sphinx', 'sphinx-copybutton', 'sphinx_markdown_tables', \
     'sphinx_rtd_theme','sphinx-autobuild', 'recommonmark']


templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_theme
html_theme = 'stanford_theme'
html_theme_path = [sphinx_theme.get_html_theme_path('stanford-theme')]

# import sphinx_bernard_theme
# html_theme = 'sphinx_bernard_theme'
# html_theme_path = [sphinx_bernard_theme.get_html_theme_path()]

html_static_path = ['_static']
html_logo = "_static/yolov6_logo.png"
#html_theme_path = [sphinx_bernard_theme.get_html_theme_path()]

# html_theme = 'alabaster'
# html_static_path = ['_static']

extensions = [
     'recommonmark',
     'sphinx_markdown_tables'
]
