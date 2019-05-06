import matplotlib.pyplot as plt
import sys

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

if __name__ == "__main__":

    mode = sys.argv[1]
    filename = sys.argv[2]

    with open(filename) as mazefile:
        if mode == "s":  plot(mazefile.read().split("\n")[:-1])
        else: plot(mazefile.read().split("\n"))

