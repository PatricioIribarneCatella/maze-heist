class MazeGraph():

    adjacency_lists = None
    height = None
    width = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.adjacency_lists = [[self._neighbours_of((i,j)) for j in range(width)] for i in range(height)] 

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
    
    def _getAdjacencyList(self, position):
        i, j = position
        return self.adjacency_lists[i][j]

    def canGo(self, _from, _to):
        return _to in self._getAdjacencyList(_from)

    def _addWall(self, position, otherPosition):
        try:
            self._getAdjacencyList(position).remove(otherPosition)
        except:
            pass
        try:
            self._getAdjacencyList(otherPosition).remove(position)
        except:
            pass
    
    def _removeWall(self, position, otherPosition):
        
        if otherPosition not in self._getAdjacencyList(position):
            self._getAdjacencyList(position).append(otherPosition)
        
        if position not in self._getAdjacencyList(otherPosition):
            self._getAdjacencyList(otherPosition).append(position)

    def toString(self):
        # Pairs are where walls or paths are going to be
        charMatrix = [
            [self._getAPrioriCharacter((i, j)) for j in range(self.width * 2 + 1)] 
            for i in range(self.height * 2 + 1)]

        for i in range(self.height):
            for j in range(self.width):
                currentPosition = (i, j)
                bottomPosition = (i + 1, j)
                rightPosition = (i, j + 1)

                # Bottom 
                if not self.canGo(currentPosition, bottomPosition) and i < self.height - 1:
                    iInMatrix, jInMatrix = self._intermediateCell(currentPosition, bottomPosition)
                    charMatrix[iInMatrix][jInMatrix] = "-"

                # Right
                if not self.canGo(currentPosition, rightPosition) and j < self.width - 1:
                    iInMatrix, jInMatrix = self._intermediateCell(currentPosition, rightPosition)
                    charMatrix[iInMatrix][jInMatrix] = "|"

        lines = map(lambda x: "".join(x), charMatrix)

        return "\n".join(lines)
 
    # Expected neighbours, undefined behaviour if not
    def _intermediateCell(self, position, otherPosition):
        
        i, j = position
        otherI, otherJ = otherPosition
        deltaI, deltaJ = (otherI - i, otherJ - j)
        
        return i * 2 + 1 + deltaI, j * 2 + 1 + deltaJ

    def _getAPrioriCharacter(self, positionInMatrix):
        
        i, j = positionInMatrix

        # Start
        if i == 0 and j == 1:
            return " "

        # Finish
        if i == self.height * 2 and j == self.width * 2 - 1 :
            return " "

        # Iterjection
        if j % 2 == 0 and i % 2 == 0:
            return "+"
        
        # Horizontal walls
        if i == 0 or i == self.height * 2:
            return "-"
        
        # Vertical wall
        if j == 0 or j == self.width * 2:
            return "|"        
        
        return " "

if __name__ == '__main__':
    
    a = MazeGraph(10, 10)

    print(a.toString())

