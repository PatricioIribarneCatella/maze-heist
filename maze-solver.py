#! /usr/bin/env python3

import sys

from solver import MazeSolver
from maze_plot import plot

FILE_INPUT = "mapa-laberinto.txt"
FILE_OUTPUT = "solucion-laberinto.txt"

def write_maze(maze):

    with open(FILE_OUTPUT, "w") as f:
        f.write(maze)

def main(path):

    ms = MazeSolver(path)

    ms.solve()
    mazeStr = ms.toString()
    write_maze(mazeStr)
    plot(mazeStr)

def parse_input(params):

    if len(params) != 2:
        
        print("Se utiliza el valor default: {}".format(FILE_INPUT))
        print("Formato: maze-solver.py [mapa-laberinto]")
        
        r = {"file-path": FILE_INPUT}
    else:
        r = {"file-path": params[1]}

    return r

if __name__ == "__main__":

    params = parse_input(sys.argv)

    main(params["file-path"])

