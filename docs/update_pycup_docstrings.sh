#!/bin/bash

PACKAGE="/home/sid/repos/my-projects/mfbd-project/pycup/pycup"

REQUIRED_PY_FILES="__init__.py base.py npa.py pca.py top.py"
set -- $REQUIRED_PY_FILES

if [ -d $PACKAGE ]; then # check if $PACKAGE exists
  for d in $(find $PACKAGE -type d); do
    if ( [ -f $d/$1 -a -f $d/$2 -a -f $d/$3 -a -f $d/$4 -a -f $d/$5 ] ) && ( [ "$d" != "${IGNORE_DIRS[0]}" ] ); then
      echo $d
      python update_pycup_docstring.py $d
    fi
  done
fi