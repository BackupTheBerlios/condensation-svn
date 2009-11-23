#!/bin/sh

epydoc --check run-condensation.py lib condensation
epydoc --config scripts/epydoc.config

echo "cleaning up..."
find . -iregex '.*\(~\|\.pyc\)$' -delete -print

echo "Statistics:"
echo -n "Lines: "
find . -iname "*.py" | xargs cat -s | wc -l
