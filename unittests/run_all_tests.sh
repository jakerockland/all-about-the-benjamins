#!/bin/bash
for f in *tests.py; do python "$f"; done
for f in predictors_tests/*tests.py; do python "$f"; done 
