import random

from graph import MazeGraph

class DFSMaze(MazeGraph):

    def _dfs_circuit(self, position, visited):

        visited[position] = True

        neighbours = self._neighbours_of(position)

        random.shuffle(neighbours)

        for t in neighbours:
            if not visited[t]:
                self._removeWall(position, t)
                self._dfs_circuit(t, visited)

    def create(self):

        visited = {(i, j):False for j in range(self.width) for i in range(self.height)}

        # Nothing is accesible at first
        self.adjacency_lists = [[[] for j in range(self.width)] for i in range(self.height)] 

        # Obtains the DFS circuit (tree)
        # while removing the edges (walls)
        # that connects two cells
        #
        self._dfs_circuit((0, 0), visited)

