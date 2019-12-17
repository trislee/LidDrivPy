# -*- coding: utf-8 -*-
#
# PyCUP documentation build configuration file.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys
sys.path.insert( 0, os.path.join(os.path.dirname(__name__), '..' ) )


# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.

needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary' ]

# Add any paths that contain templates here, relative to this directory.
templates_path = [ '_templates' ]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string.
source_suffix = [ '.rst', ]

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'PyCUP'
copyright = u'2019, Nanohmics, Inc.'
author = u'Nanohmics, Inc.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
version = u'1.0'

# The full version, including alpha/beta/rc tags.
release = u'1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
  '_build', 'Thumbs.db', '.DS_Store' ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, figures, tables and code-blocks are automatically numbered if
# they have a caption. At same time, the numref role is enabled. For now,
# it works only with the HTML builder and LaTeX builder. Default is False.
numfig = True


# -- Napoleon extension parameters ---------------------------------------------

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_use_keyword = True
napoleon_custom_sections = [
  'Initialization Parameters',
  'Execution Parameters' ]

# -- Autodoc extension parameters ----------------------------------------------

# This value is a list of autodoc directive flags that should be automatically
# applied to all autodoc directives. The supported flags are 'members',
# 'undoc-members', 'private-members', 'special-members', 'inherited-members'
# and 'show-inheritance'.
autodoc_default_flags = [
  'private-members',
  'show-inheritance' ]

autodoc_member_order = 'bysource'
autoclass_content = 'both'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_favicon = 'figs/favicon.ico'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#   "navigation_depth" : 1
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [  ]


# -- Options for HTMLHelp output -----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyCUPdoc'


# -- Options for LaTeX output --------------------------------------------------

# A dictionary that contains LaTeX snippets that override those Sphinx usually
# puts into the generated .tex files.
# Keep in mind that backslashes must be doubled in Python string literals to
# avoid interpretation as escape sequences.
latex_elements = {
  'papersize': 'letterpaper',
  'fontpkg': '',
  'fncychap': '\\usepackage[Sonny]{fncychap}',
  'maketitle': '\\maketitle',
  'pointsize': '11pt',
  'preamble': '\\renewcommand{\\textbar}{|}', # fix warnings with some fonts
  'releasename': '',
  'babel': '',
  'printindex': '',
  'fontenc': '',
  'inputenc': '',
  'classoptions': '',
  'utf8extra': '',
  'figure_align': 'htbp',
  'extraclassoptions': 'openany', # remove even/odd blank pages
  'sphinxsetup':
    'TitleColor={rgb}{0,0,0},' +
    'InnerLinkColor={rgb}{0.10,0.10,0.44},' +
    'OuterLinkColor={rgb}{0.10,0.10,0.44}' }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ( master_doc,
    u'PyCUP.tex',
    u'PyCUP Documentation',
    u'Nanohmics, Inc.',
    u'manual',
    True ), ]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
  ( master_doc,
    u'PyCUP',
    u'PyCUP Documentation',
    [ u'Nanohmics, Inc.' ],
    1 ) ]


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ( master_doc,
    u'PyCUP',
    u'PyCUP Documentation',
    u'Nanohmics, Inc.',
    u'PyCUP',
    u'Collection of routines for performing mathematical operations '
      + u'on arrays and stacks of arrays using CUDA.'
    u'Main'), ]