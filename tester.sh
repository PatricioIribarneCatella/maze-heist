#!/bin/bash
for i in {0..100}
 do 
     python3.7 maze-generator.py dyc 30 30
     python3.7 maze-solver.py
 done


for i in {0..100}
 do 
     python3.7 maze-generator.py dfs 30 30
     python3.7 maze-solver.py
 done


