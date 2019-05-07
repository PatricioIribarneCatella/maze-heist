#! /usr/bin/env python3

import sys
import matplotlib.pyplot as plt

FILE_SOL = "solucion-laberinto.txt"
FILE_MAP = "mapa-laberinto.txt"

def char2plot(c):
    # spaces = 2s, path = 1s,  walls = 0s
    if c == ' ': return 2
    if c == '*': return 1
    return 0

def plot(lines):

    maze = [[char2plot(c) for c in line] for line in lines]
    
    plt.pcolormesh(maze, cmap='gray')
    plt.axes().set_aspect('equal') 
    
    plt.xticks([]) 
    plt.yticks([])
    
    plt.axes().invert_yaxis() 
    
    plt.show()

def main(path, file_type):

    with open(path) as mazefile:
        if file_type == "s":
            plot(mazefile.read().split("\n")[:-1])
        elif file_type == "m":
            plot(mazefile.read().split("\n"))

def parse_input(params):

    if len(params) < 2:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: maze-plot.py [tipo-mapa] [archivo](opcional)")
        print("Default:")
        print("\t[archivo]: mapa-laberinto.txt si tipo-mapa == 'm'")
        print("\t[archivo]: solucion-laberinto.txt si tipo-mapa == 's'")
        return None

    file_type = params[1]

    if file_type not in ["s", "m"]:
        print("Tipo de mapa incorrecto: tiene que ser 'm': mapa o 's': solución")
        return None

    if len(params) == 2:
        path = FILE_MAP if file_type == "m" else FILE_SOL
    else:
        path = params[2]

    return {"path": path,
            "type": file_type}

if __name__ == "__main__":

    params = parse_input(sys.argv)

    if params is not None:
        main(params["path"], params["type"])


