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

    def _fillHorizontalWalls(self, idx, line):
       
        # Find out which horizontal
        # row is
        idx = idx // 2

        r = list(enumerate(line))

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
        for c in cells:
            self._addWall((idx, c - 1), (idx, c))

    def _fillVerticalWalls(self, idx, line):
        
        # Find out which vertical
        # row is.
        # This number represents which
        # two cells have to be connected
        # or not. For example:
        # if idx == 0 then it represents
        # cells in the 'zero' row and in
        # the 'one' row.
        idx = idx // 2

        r = list(enumerate(line))

        # Remove first '+'
        r = r[1:]

        # Remove last '+'
        r.pop()

        # Remove all spaces
        r = list(filter(lambda x: x[1] == '-', r))

        # Calculate indexes where walls
        # must be placed in
        cells = list(map(lambda x: x[0] // 2, r))

        # Iterate cells and add walls
        for c in cells:
            self._addWall((idx, c), (idx + 1, c))


    # From lines in the map
    # reconstructs the maze
    def _fillWalls(self, lines):

        # Remove first and last
        # lines that corresponds
        # to the first and last 
        # horizontal walls
        lines = lines[1:]
        lines.pop()

        for l in enumerate(lines):

            idx, line = l

            if line.startswith("|"):
                self._fillHorizontalWalls(idx, line)

            if line.startswith("+"):
                self._fillVerticalWalls(idx, line)

    def solve(self):
        print("not implemented")
        

