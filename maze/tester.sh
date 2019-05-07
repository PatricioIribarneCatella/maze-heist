#!/bin/bash

PYVER=$(python3 --version | sed 's/^.* //g' | cut -f2 -d.)

for i in {0..100}
 do 
     python3.$PYVER maze-generator.py dyc 30 30
     python3.$PYVER maze-solver.py
 done


for i in {0..100}
 do 
     python3.$PYVER maze-generator.py dfs 30 30
     python3.$PYVER maze-solver.py
 done


