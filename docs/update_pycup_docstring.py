# -*- coding: utf-8 -*-

"""Updates PyCUP docstrings from previous iteration (2019-09-03) all in one go.
"""

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import sys
import os
from pathlib import Path
import re
from typing import Union, Sequence

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

DEFAULT_INIT_PARAMS = (
  'shape',
  'noid',
  'dtype',
  'order',
  'acls'
)

DEFAULT_INIT_PARAMS_DOCSTRING = \
  r'  * **shape** *(tuple)* --\n' + \
  r'    Nominal array shape of the operation.\n' + \
  r'\n' + \
  r'  * **noid** *(int, optional)* --\n' + \
  r'    Number of independent dimensions.\n' + \
  r'    Default inherited from parent class\n' + \
  r'\n' + \
  r'  * **dtype** *(np.dtype, optional)* --\n' + \
  r'    Nominal dtype of the operation.\n' + \
  r'    Supported values defined in the class variable ``_supported_dtypes``.\n'+\
  r'    Defaults to first entry of ``_supported_dtypes``.\n' + \
  r'\n' + \
  r'  * **order** *(string, optional)* --\n' + \
  r"    Major order of compatible arrays, ``{'c','f','forc'}``.\n" + \
  r'    Supported values defined in the class variable ``_supported_orders``.\n'+\
  r'    Defaults to first entry of ``_supported_orders``.\n' + \
  r'\n' + \
  r'  * **acls** *(class object, optional)* --\n' + \
  r'    Class of compatible arrays. Supported values defined in the class variable\n' + \
  r'    through the list ``_supported_aclss``.\n' + \
  r'    Defaults to first entry of ``_supported_aclss``.\n'

DEFAULT_EXEC_PARAMS_DOCSTRING = {
  'x' : r'  * **x** *(array)* --\n' + \
        r'    Input / output container of independent arrays.\n', \
  'y' : r'  * **y** *(array)* --\n' + \
        r'    Input container of independent arrays.\n', \
  'z' : r'  * **z** *(array)* --\n' + \
        r'    Input container of independent arrays.\n', \
  'u' : r'  * **u** *(array)* --\n' + \
        r'    Input independent array.\n', \
  'v' : r'  * **v** *(array)* --\n' + \
        r'    Input independent array.\n', \
  'a' : r'  * **a** *(array)* --\n' + \
        r'    Input container of independent scalars.\n', \
  'b' : r'  * **b** *(array)* --\n' + \
        r'    Input container of independent scalars.\n', \
  'c' : r'  * **c** *(array)* --\n' + \
        r'    Input container of independent scalars.\n', \
  'd' : r'  * **d** *(scalar)* --\n' + \
        r'    Input scalar.\n', \
  'e' : r'  * **e** *(scalar)* --\n' + \
        r'    Input scalar.\n'
}

MISC_EXEC_PARAMS_DOCSTRING = {
  'rfftsum' : { 'out' : r'  * **out** *(array)* --\n' + \
                        r'    Result of reduction operation.\n' }
}

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def find_regex_match(
  path: Union[ str, Path ] = None,
  string: str = None,
  re_const: bool = None,
  regex: str = r''
):

  assert path is not None or string is not None

  if path:
    with open( path, 'r' ) as f:
      f_string = f.read()
      if re_const: match = re.findall( regex, f_string, re_const )
      else: match = re.findall( regex, f_string )
  elif string:
    if re_const: match = re.findall( regex, string, re_const )
    else: match = re.findall( regex, string )
  # if len( match ) > 1:
  #   raise IndexError( f'More than one match of {match} found!' )

  return match

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_init_params( path: Union[ str, Path ] ):

  _regex_params_eng = r'\n *(\w+?) = '
  _regex_eng = r'# instantiate engine\n  eng = ' + \
               r'instantiate_engine(\(.*\))\n\n  # execute engine\n  '
  eng_match = find_regex_match( \
    path = path, re_const = re.DOTALL, regex = _regex_eng )
  init_params = \
    [ param for param in re.findall( _regex_params_eng, eng_match[0] ) ]

  _def_init_params = [ init_param for init_param in init_params if \
                       init_param in DEFAULT_INIT_PARAMS ]
  _ext_init_params = [ init_param for init_param in init_params if \
                       init_param not in DEFAULT_INIT_PARAMS ]
  if set( _def_init_params ) != set( DEFAULT_INIT_PARAMS ):
    raise ValueError( f'Module {path} does not contain all of the default ' + \
                      f'init params {DEFAULT_INIT_PARAMS}.' )

  init_params = list( DEFAULT_INIT_PARAMS ) + _ext_init_params

  #----------------------------------------------------------------------------#

  _regex_params_out = r' *(\w+?) = '
  _regex_out = r'# execute engine\n  .*?eng\.execute(\(.*\))\n\n.*?'+ \
               r'def select_engine_class\('
  out_match = find_regex_match( \
    path = path, re_const = re.DOTALL, regex = _regex_out )

  exec_params = \
    [ param for param in re.findall( _regex_params_out, out_match[0] ) ]

  #----------------------------------------------------------------------------#

  return ( init_params, exec_params, )

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def replace_base_cls_link_init( path: Union[ str, Path ], base_class: str ):

  with open( path, 'r+' ) as f:
    f_string = f.read()
    f.seek(0)
    orig = fr'(`{base_class}`)' + r'([\s\S]*?)\n([^\n]{,15}) '
    repl = fr'\n:py:class:`base.{base_class}`'
    f.write( re.sub( orig, fr'{repl}\2 \3\n', f_string, flags = re.DOTALL ) )
    f.truncate()

def gen_init_docstring(
  path: Union[ str, Path ],
  init_params_ds_lst: str,
  exec_params_ds_lst: str
):
  with open( path, 'r+' ) as f:
    f_string = f.read()
    f.seek(0)
    orig = r'\n *Examples\n *\-+\n'
    _cond_newlines = r'\n' if init_params_ds_lst else r''
    repl = \
      r'\nInitialization Parameters\n-------------------------\n\n' + \
      DEFAULT_INIT_PARAMS_DOCSTRING + \
      _cond_newlines + \
      r'\n'.join( init_params_ds_lst ) + \
      r'\nExecution Parameters\n--------------------\n\n' + \
      r'\n'.join( exec_params_ds_lst ) + \
      re.findall( orig, f_string )[0]
    f.write( re.sub( orig, repl, f_string ) )
    f.truncate()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def get_init_params_docstring( \
  path:Union[ str, Path ], params:Sequence, regex:str ):

  ref_docstring = find_regex_match( \
    path = path, re_const = re.DOTALL, regex = regex )

  params_docstring_lst = []
  for non_def_param in params:
    _caught = find_regex_match(  \
      string = ref_docstring[0],
      regex = fr'  {non_def_param} : (.+)\n *(.+)'
    )
    _repl = fr'  * **{non_def_param}** *({_caught[0][0]})* --\n' + \
            fr'    {_caught[0][1]}\n'

    params_docstring_lst.append( _repl )

  return params_docstring_lst

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def iterate_docstrings_init_gen( path: Union[ str, Path ], params: Sequence ):

  path = Path( path )

  _regex_subroutine = r'def subroutine\(.+?(""".*?""").+?' + \
                      r'def select_engine_class\('

  init_params_ds_lst = get_init_params_docstring( \
    path, params[0][ len( DEFAULT_INIT_PARAMS ): ], _regex_subroutine )

  #----------------------------------------------------------------------------#

  _misc_exec_params_docstring = \
    MISC_EXEC_PARAMS_DOCSTRING[ path.parts[-2] ] if \
    path.parts[-2] in MISC_EXEC_PARAMS_DOCSTRING else {}
  _exec_params_def_ds = [ DEFAULT_EXEC_PARAMS_DOCSTRING[ exec_param ] for \
                          exec_param in params[1] if \
                          exec_param in DEFAULT_EXEC_PARAMS_DOCSTRING ]
  _exec_params_ext = [ exec_param for exec_param in params[1] if exec_param \
                       not in DEFAULT_EXEC_PARAMS_DOCSTRING and exec_param \
                       not in _misc_exec_params_docstring ]
  _exec_params_ext_ds = get_init_params_docstring( \
    path, _exec_params_ext, _regex_subroutine
  )
  _exec_params_misc_ds = []
  if _misc_exec_params_docstring:
    _exec_params_misc_ds.extend(
      [ _misc_exec_params_docstring[ exec_param ] for \
        exec_param in params[1] if exec_param in \
        _misc_exec_params_docstring ]
    )

  exec_params_ds_lst = \
    _exec_params_def_ds + \
    _exec_params_ext_ds + \
    _exec_params_misc_ds

  #----------------------------------------------------------------------------#

  gen_init_docstring(
    path.parent/'__init__.py', \
    init_params_ds_lst,
    exec_params_ds_lst
  )

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def replace_old_docstrings( dir: Union[ str, Path ] ):
  # TODO: Add assertion where this can only be done if
  #       `iterate_docstrings_init_gen` is implemented first. Otherwise unsafe.

  dir = Path( dir )

  path_base = dir/'base.py'
  path_top = dir/'top.py'

  repl_root = re.findall( \
    r'/(pycup/.*)', RAW_DIR )[0].replace( "/", "." )[ len('pycup.'): ]
  repl_root_ds = fr'  arguments :\n    See :py:mod:`{repl_root}`'

  #----------------------------------------------------------------------------#

  _regex_base_class = r'class (\w+?)\(.*:'
  _regex_base = r'(class \w+?\(.*:.*?""".*\n)' + \
                r'(.*?""".*?def __init__\(.*?\):(?:(?!""").)*?)' + \
                r'.*?((?:(?!"+).)+$)'
  _params_raw = r'Parameters\n  ----------\n'
  with open( path_base, 'r+' ) as f:
    f_string = f.read()
    base_class = re.findall( _regex_base_class, f_string )[0]
    orig_base = find_regex_match( string = f_string, re_const = re.DOTALL, \
                                  regex = _regex_base )
    if orig_base:
      if r'def __init__(' in orig_base[0][1]:
        f.seek(0)
        f.write( re.sub( \
          _regex_base, fr'\1\n  {_params_raw}{repl_root_ds}\n\n\2\3', \
          f_string, flags = re.DOTALL ) )
        f.truncate()

  #----------------------------------------------------------------------------#

  _subsubregex_top_params = r'( *""".*Parameters\n *----------\n).*?' + \
                            r'(\n\n *Returns\n *-------\n)'
  _subregex_top_params = _subsubregex_top_params + \
                         r'(.*? *See Also\n *--------).+?"""'
  with open( path_top, 'r+' ) as f:
    f_string = f.read()
    f.seek(0)
    _regex_subroutine_params = fr'(def subroutine\(.+?)' + \
                               fr'{_subsubregex_top_params}' + \
                               fr'(.+?def select_engine_class\()'
    f.write( \
      re.sub(_regex_subroutine_params, fr'\1\2{repl_root_ds}\3\4', \
              f_string, flags = re.DOTALL )
    )
    f.truncate()

  with open( path_top, 'r+' ) as f:
    f_string = f.read()
    f.seek(0)
    _regex_insteng_params = fr'(def instantiate_engine\(.+?)' + \
                            fr'{_subregex_top_params}' + \
                            fr'(.+?return engine)'
    repl_see_also = fr'\n  {repl_root}.base.{base_class}' + \
                    fr'\n  {repl_root}.npa.{base_class}Npa' + \
                    fr'\n  {repl_root}.pca.{base_class}Pca\n\n  """'
    f.write( re.sub( _regex_insteng_params, \
                     fr'\1\2{repl_root_ds}\3\4{repl_see_also}\5', \
                     f_string, flags = re.DOTALL )
    )
    f.truncate()

  with open( path_top, 'r+' ) as f:
    f_string = f.read()
    f.seek(0)
    _utf = r'\# -\*- coding: UTF-8 -\*-'
    f.write( re.sub( \
      fr'({_utf}\n)\n\#\++?\#\n(.*)', r'\1\2', f_string, flags = re.DOTALL )
    )
    f.truncate()

  return base_class

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def update_low_level_docstrings( dir: Union[ str, Path ] ):

  params = get_init_params( dir/'top.py' )
  iterate_docstrings_init_gen( dir/'top.py', params )
  base_class = replace_old_docstrings( dir )


  replace_base_cls_link_init( dir/'__init__.py', base_class )

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

if __name__ == '__main__':

  RAW_DIR = os.path.abspath( sys.argv[1] )
  DIR = Path( str( RAW_DIR ) )

  update_low_level_docstrings( DIR )

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
