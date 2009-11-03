#!/bin/sh

epydoc --check drupaladmin.py da
epydoc --config scripts/epydoc.config

echo "cleaning up..."
find . -iname "*~" -o -iname "*.pyc" -delete -print

echo "Statistics:"
echo -n "Lines: "
find . -iname "*.py" | xargs cat -s | wc -l
