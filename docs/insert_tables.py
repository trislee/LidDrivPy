# -*- coding: UTF-8 -*-

"""Testing for parsing the directory of Sphinx source documents
"""

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import os

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def capitalize(string, n = 1):

  """Capitalizes the first `n` characters in a string
  """

  if n == -1:
    return string.upper()
  else:
    return string[:n].upper() + string[n:].lower()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def select_n(string, subpackage):

  """Based on the PyCUP Engine naming convention, selects the correct number of
  characters to capitalize for a given operation and subpackage
  """

  _subpackage = subpackage.lower()
  _string = string.lower()

  if _subpackage in ('elemental', 'ndops', 'misc'):
    return -1
  else:
    if _subpackage == 'fft':
      if string.startswith('r'):
        return 2
      else:
        return 1
    elif _subpackage == 'reduction':
      if string.startswith(('bi',)):
        return 1
      elif string.startswith(('rffts')):
        return 5
      elif _string.startswith(('b', 'am')):
        return 2
      else:
        return 1
    else:
      raise ValueError(f'invalid subpackage name: {_subpackage}')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# directory containing *.rst source files
pardir = 'source/'

# any file ending with these strings is not the base of an operation subpackage
ignore_ends = (
  'base.rst',
  'npa.rst',
  'pca.rst',
  'top.rst',
  'elemental.rst',
  'intrinsic.rst',
  'derived.rst',
  'fft.rst',
  'ndops.rst',
  'reduction.rst',
  'gpu.rst',
  'base.rst',
  'gpu.rst',
  'utils.rst',
  'pycup.rst'
)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

if __name__ == '__main__':

  files = sorted(os.listdir(pardir))

  filtered_files = [f for f in files if not f.endswith(ignore_ends)]

  for file in filtered_files:

    # split filename into separate levels e.g. (pycup, elemental, derived, xpa, rst)
    splits = file.split('.')
    string = splits[-2]
    subpackage = splits[1]

    # get path to functions for linking, and length of longest function name
    function = file.strip('.rst') + '.top'
    function_length = len(':py:func:`select_engine_class() <.select_engine_class`>' + function)

    # correctly capitalize the engine name to match the actual names in the package
    n = select_n(string = string, subpackage = subpackage)

    _string = capitalize(string = string, n = n)

    # fft subpackage is capitalized, unlike other subpackage names
    if subpackage.lower() == 'fft':
      _subpackage = capitalize(string = subpackage, n = -1)
    else:
      _subpackage = capitalize(string = subpackage, n = 1)

    engine = _subpackage + _string
    engine_length = len(':py:class:`.EngineNpa`' + engine)

    # text of the table that's inserted into the source *.rst files
    value = f"""\nHigh-level Interface Functions
------------------------------
.. table::
  :align: left
  :widths: 10 10

  {'='*function_length}  ==============================
  :py:func:`subroutine() <{function}.subroutine>`                    perform elemental operations
  :py:func:`instantiate_engine() <{function}.instantiate_engine>`    return instantiated engine
  :py:func:`select_engine_class() <{function}.select_engine_class>`  return compatible engine class
  {'='*function_length}  ==============================

Classes
-------
.. table::
  :align: left
  :widths: 10 10

  {'='*engine_length}  ==============================
  :py:class:`.Engine{engine}`     Engine class
  :py:class:`.Engine{engine}Npa`  Engine class for NumPy arrays
  :py:class:`.Engine{engine}Pca`  Engine class for PyCUDA arrays
  {'='*engine_length}  ==============================\n"""

    # initialize line number to insert table into
    index = None

    # read contents of source *.rst file
    with open(os.path.join(pardir, file), 'r') as f:
      contents = f.readlines()

    # find line number at which to insert table
    for i, line in enumerate(contents):
      if line.rstrip() == 'Submodules':
        index = i - 1

    # insert table at given line number
    contents.insert(index, value)

    # write new contents to file
    with open(os.path.join(pardir, file), 'w') as f:
      f.writelines(contents)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#