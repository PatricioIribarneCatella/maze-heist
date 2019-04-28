import random

from graph import MazeGraph

class DFSMaze(MazeGraph):

    def create(self):
        self._create(0, self.width - 1, 0, self.height - 1)

    def _create(self, startWidth, finishWidth, startHeight, finishHeight):

        visited = {(i, j):False for j in range(self.width) for i in range(self.height)}

        res = []

        # Obtains the DFS circuit (tree)
        # while removing the edges (walls)
        # that connects two cells
        self._dfs_circuit((startWidth, startHeight), visited, res)

    def _dfs_circuit(self, position, visited, res):

        res.append(position)

        visited[position] = True

        neighbours = self._getAdjacencyList(position)

        random.shuffle(neighbours)

        for t in neighbours:
            if not visited[t]:
                self._addWall(position, t)
                self._dfs_circuit(t, visited, res)

if __name__ == '__main__':

    a = DFSMaze(10, 10)

    a.create()

    print(a.toString())

