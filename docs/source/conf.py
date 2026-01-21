import os
import sys
# Ensure that Sphinx can find and import the necessary Python
sys.path.insert(0, os.path.abspath('../'))
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python Package'
copyright = '2026, Skander Adam Afi'
author = 'Skander Adam Afi'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
 'sphinx.ext.autodoc',
 'sphinx.ext.viewcode',
 'sphinx.ext.napoleon',
 'sphinx.ext.githubpages'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
