import random

from graph import MazeGraph

TOP = 1
RIGHT = 2
BOTTOM = 3
LEFT = 4

class DACMaze(MazeGraph):

    def _create(self, startWidth, finishWidth, startHeight, finishHeight):
       
        if (startWidth == finishWidth or startHeight == finishHeight):
            return
        
        # Where there will be walls
        divisorWidth = random.randrange(startWidth, finishWidth)
        divisorHeight = random.randrange(startHeight, finishHeight)

        # Add the walls and its holes
        missingHole = random.choice([TOP, RIGHT, BOTTOM, LEFT])

        self._blockRight(divisorWidth, divisorHeight,  startHeight, finishHeight, missingHole)
        self._blockBottom(divisorWidth, divisorHeight, startWidth, finishWidth, missingHole)
        
        # Divide
        self._create(startWidth, divisorWidth, startHeight, divisorHeight) #TopLeft
        self._create(divisorWidth + 1, finishWidth, startHeight, divisorHeight) #TopRight
        self._create(startWidth, divisorWidth, divisorHeight + 1, finishHeight) # BottomLeft
        self._create(divisorWidth + 1, finishWidth, divisorHeight + 1, finishHeight) # BottomRight

    def _blockRight(self, blockingWidth, blockingHeight, startHeight, finishHeight, missingHole):
        
        for height in range(startHeight, finishHeight + 1): # Block everything
            self._addWall((height, blockingWidth), (height, blockingWidth + 1))

        if missingHole != TOP:
            heightAccessTop = random.randint(startHeight, blockingHeight) # Make first "half" hole
            self._removeWall((heightAccessTop, blockingWidth), (heightAccessTop, blockingWidth + 1))

        if missingHole != BOTTOM:
            heightAccessBottom = random.randint(blockingHeight + 1, finishHeight) # Make second "half" hole
            self._removeWall((heightAccessBottom, blockingWidth), (heightAccessBottom, blockingWidth + 1))

    def _blockBottom(self, blockingWidth, blockingHeight, startWidth, finishWidth, missingHole):
        
        for width in range(startWidth, finishWidth + 1): # Block everything
            self._addWall((blockingHeight, width), (blockingHeight + 1, width))

        if missingHole != LEFT:
            widthAccessLeft = random.randint(startWidth, blockingWidth) # Make first "half" hole
            self._removeWall((blockingHeight, widthAccessLeft), (blockingHeight + 1, widthAccessLeft))

        if missingHole != RIGHT:
            widthAccessRight = random.randint(blockingWidth + 1, finishWidth) # Make second "half" hole
            self._removeWall((blockingHeight, widthAccessRight), (blockingHeight + 1, widthAccessRight))

    def create(self):
        self._create(0, self.width - 1, 0, self.height - 1)

