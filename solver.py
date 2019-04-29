class MazeSolver():

    def __init__(self, path):

        with open(path, "r") as f:
            lines = f.readlines()

        for l in lines:
            print("l: {}".format(l))

    def solve(self):
        print("not implemented")
        
    def toString(self):
        print("not implemented")
        return ""

