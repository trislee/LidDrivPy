# -*- coding: UTF-8 -*-

import os.path
from setuptools import setup

def readme( ):

  with open( os.path.abspath(
    os.path.join(
      os.path.dirname( __file__ ),
      'README.rst' ) ) ) as f:

    return f.read( )

setup(
  name = 'liddrivpy',
  version = '0.1',
  description = 'Python Cuda Primitives',
  long_description = readme( ),
  author = 'Nanohmics, Inc.',
  author_email = 'software.support@nanohmics.com',
  packages = [
    'liddrivpy'
    ],
  test_suite = 'tests.test_suite',
  dependency_links = [ ],
  install_requires = [
    'numpy >= 1.16',
    'matplotlib >= 3.1.0' ],
  extras_require = {
    'docs': [
      'sphinx >= 2.1',
      'sphinx_rtd_theme >= 0.4', ] },
  include_package_data = True,
  zip_safe = False )
