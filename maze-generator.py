#! /usr/bin/env python3

import sys

from dfs_maze import DFSMaze
from dac_maze import DACMaze

FILE_OUTPUT = "mapa-laberinto.txt"
DFS = "dfs"
DAC = "dyc"

def write_maze(maze):

    with open(FILE_OUTPUT, "w") as f:
        f.write(maze)

def main(method, height, width):

    if method == DFS:
        maze = DFSMaze(width, height)
    elif method == DAC:
        maze = DACMaze(width, height)

    maze.create()

    write_maze(maze.toString())

def parse_input(params):

    if len(params) != 4:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: maze-generator.py [metodo] [largo] [ancho]")
        return None

    method = params[1]

    if method not in ["dyc", "dfs"]:
        print("Método incorrecto: tiene que ser 'dfs' o 'dyc'")
        return None

    height = params[2]
    width = params[3]

    if not height.isdigit() or not width.isdigit():
        print("Largo o Ancho incorrecto: deben ser números enteros")
        return None

    height = int(height)
    width = int(width)

    if height <= 0 or width <= 0:
        print("Largo o ancho inválido: deben ser enteros positivos")
        return None

    return {"method": method,
            "height": height,
            "width": width
            }

if __name__ == "__main__":

    params = parse_input(sys.argv)

    if params is not None:
        main(params["method"],
                params["height"],
                params["width"])

