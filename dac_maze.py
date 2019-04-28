import random

from graph import MazeGraph

class DACMaze(MazeGraph):
    def create(self):
        self._create(0, self.width - 1, 0, self.height - 1) #Esto esta mal creo Revisar
        

    def _create(self, startWidth, finishWidth, startHeight, finishHeight):
        if (startWidth == finishWidth or startHeight == finishHeight ):
            return
        # Where there will be walls
        divisorWidth = random.randrange(startWidth, finishWidth)
        divisorHeight = random.randrange(startHeight, finishHeight)

        # Add the walls and its holes
        self._blockRight(divisorWidth, divisorHeight,  startHeight, finishHeight)
        self._blockBottom(divisorWidth, divisorHeight, startWidth, finishWidth)
        
        # Divide
        self._create(startWidth, divisorWidth, startHeight, divisorHeight) #TopLeft
        self._create(divisorWidth + 1, finishWidth, startHeight, divisorHeight) #TopRight
        self._create(startWidth, finishWidth, divisorHeight + 1, finishHeight) # BottomLeft
        self._create(divisorWidth + 1, finishWidth, divisorHeight + 1, finishHeight) # BottomRight

    def _blockRight(self, blockingWidth, blockingHeight, startHeight, finishHeight):
        
        for height in range(startHeight, finishHeight): # Block everything
            self._addWall((height, blockingWidth), (height, blockingWidth + 1))

        heightAccessTop = random.randint(startHeight, blockingHeight) # Make first "half" hole MAYBE UNNECESSARY
        self._removeWall((heightAccessTop, blockingWidth), (heightAccessTop, blockingWidth + 1))

        heightAccessBottom = random.randint(blockingHeight + 1, finishHeight) # Make second "half" hole
        self._removeWall((heightAccessBottom, blockingWidth), (heightAccessBottom, blockingWidth + 1))

    def _blockBottom(self, blockingWidth, blockingHeight, startWidth, finishWidth):
        
        for width in range(startWidth, finishWidth): # Block everything
            self._addWall((blockingHeight, width), (blockingHeight + 1, width))

        widthAccessLeft = random.randint(startWidth, blockingWidth) # Make first "half" hole
        self._removeWall((blockingHeight, widthAccessLeft), (blockingHeight + 1, widthAccessLeft))

        widthAccessRight = random.randint(blockingWidth + 1, finishWidth) # Make second "half" hole
        print (blockingHeight, widthAccessRight)
        self._removeWall((blockingHeight, widthAccessRight), (blockingHeight + 1, widthAccessRight))

if __name__ == '__main__':
    a = DACMaze(30,30)

    a.create()

    # for l in a:
    #     print(l)

    print(a.toString())