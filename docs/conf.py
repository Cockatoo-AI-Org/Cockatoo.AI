# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../sample_py_files'))
# Note: if use '../../' instead, one should then use sample_py_files.stlmodel whenever calling .. automodules:
# However, this still doesn't work since the stlmodel.py will try to import metrics.py and helpers.py, but since 
# sample_py_files path is not in sys, so the import fails.

# print(sys.path)


# -- Project information -----------------------------------------------------

project = 'stl_model_doc'
copyright = '2021, Kai'
author = 'Kai'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 
    "sphinx.ext.napoleon", 
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme", 
    "sphinxarg.ext"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# document both the class and init docstrings 
autoclass_content = 'both'
# napoleon style 
napoleon_google_docstring = True # True to parse Google style docstrings. False to disable support for Google style docstrings. Defaults to True.
napoleon_numpy_docstring = True # True to parse NumPy style docstrings. False to disable support for NumPy style docstrings. Defaults to True.
napoleon_include_init_with_doc = True # True to list __init___ docstrings separately from the class docstring. False to fall back to Sphinx’s default behavior, which considers the __init___ docstring as part of the class documentation. Defaults to False.
napoleon_include_private_with_doc = True # True to include private members (like _membername) with docstrings in the documentation. False to fall back to Sphinx’s default behavior. Defaults to False.
napoleon_include_special_with_doc = True # True to include special members (like __membername__) with docstrings in the documentation. False to fall back to Sphinx’s default behavior. Defaults to True.


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme ='sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']