import matplotlib.pyplot as plt

def char2plot(c):
    # spaces = 2s, path = 1s,  walls = 0s
    if c == ' ': return 2
    if c == '*': return 1
    return 0

def plot(maze_str):
    lines = maze_str.split('\n') 
    maze = [[char2plot(c) for c in line] for line in lines[:-1]]
    plt.pcolormesh(maze, cmap='gray')
    plt.axes().set_aspect('equal') 
    plt.xticks([]) 
    plt.yticks([])
    plt.axes().invert_yaxis() 
    plt.show()


