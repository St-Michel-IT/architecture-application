#!/usr/bin/bash
# Check lualatex is installed
if ! [ -x "$(command -v lualatex)" ]; then
  echo 'Error: lualatex is not installed.' >&2
  exit 1
fi
# cd in doc or handle error
cd doc || echo "Canot cd in doc"
# Compile LaTeX with lualatex, compile twice to get the table of contents
lualatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=build/pdf Architecture-Application-L3-CSI.tex
lualatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=build/pdf Architecture-Application-L3-CSI.tex