#!/bin/bash

ODIR="source"
PDIR="${PWD}/../pycup"

rm -fr "${ODIR}"

sphinx-apidoc \
--separate \
--private \
--module-first \
-o "${ODIR}" \
"${PDIR}"

rm -vf "${ODIR}/modules.rst"

# insert table for subpackage classes and functions
python insert_tables.py

# set subpackage toctree maxdepth to 1
perl -i -0pe "s/Subpackages\\n-----------\\n\\n.. toctree::/Subpackages\\n-----------\\n\\n.. toctree::\\n   :maxdepth: 1/" source/*.rst