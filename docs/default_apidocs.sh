#!/bin/bash

ODIR="source"
PDIR="${PWD}/../liddrivpy"

rm -fr "${ODIR}"

sphinx-apidoc \
--separate \
--private \
--module-first \
-o "${ODIR}" \
"${PDIR}"

rm -vf "${ODIR}/modules.rst"

# set subpackage toctree maxdepth to 1
perl -i -0pe "s/Subpackages\\n-----------\\n\\n.. toctree::/Subpackages\\n-----------\\n\\n.. toctree::\\n   :maxdepth: 1/" source/*.rst