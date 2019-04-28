class MazeGraph():

    adjacency_lists = None
    height = None
    width = None
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.adjacency_lists = [ [self._neighbours_of((i,j)) for j in range(width)] for i in range(height)] 

    # def _position_in_array(self, position):
    #     i, j = position
    #     return i * self.width + j
    
    def _neighbours_of(self, position):
        i, j = position
        neighbours = []
        
        if i > 0:
            neighbours.append((i - 1, j)) # Top
        if i < self.height - 1:
            neighbours.append((i + 1, j)) # Bottom
        if j > 0:
            neighbours.append((i, j - 1)) # Left
        if j < self.width - 1:
            neighbours.append((i, j + 1)) # Right

        return neighbours
    
    def getAdjacencyList(self, position):
        i, j = position
        return self.adjacency_lists[i][j]

    def _addWall(self, position, otherPosition):
        try:
            self.getAdjacencyList(position).remove(otherPosition)
        except:
            pass
        try:
            self.getAdjacencyList(otherPosition).remove(position)
        except:
            pass
    
    def _removeWall(self, position, otherPosition):
        if otherPosition not in self.getAdjacencyList(position):
            self.getAdjacencyList(position).append(otherPosition)
        if position not in self.getAdjacencyList(otherPosition):
            self.getAdjacencyList(otherPosition).append(position)


if __name__ == '__main__':
    a = MazeGraph(3,3).adjacency_lists

    for l in a:
        print(l)
