from graph import MazeGraph

class MazeSolver(MazeGraph):

    def __init__(self, path):

        with open(path, "r") as f:
            lines = f.readlines()

        first = lines[0]

        width = first.count("+") - 1
        height = len(lines) // 2

        super(MazeSolver, self).__init__(width, height)

        self._fillWalls(lines)

    def _fillHorizontalWalls(self, line):
        
        r = list(enumerate(l))

        # Remove first pipe
        r = r[1:]

        # Remove last pipe
        r.pop()

        # Remove all spaces
        r = list(filter(lambda x: x[1] == '|', r))

        # Calculate indexes where walls
        # must be placed in
        cells = list(map(lambda x: x[0] // 2, r))

        # Iterate cells and add walls

    def _fillVerticalWalls(self, line):
        print("not implemented")

    # From lines in the map
    # reconstructs the maze
    def _fillWalls(self, lines):

        for l in lines:

            if l.startswith("|"):
                self._fillHorizontalWalls(l)

            if l.startswith("+"):
                self._fillVerticalWalls(l)

    def solve(self):
        print("not implemented")
        

