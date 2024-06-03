from pos import BlockPosition as P
from tetra import Blocks

class LBlock(Blocks):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0 : [P(0,1), P(1,1), P(2,1), P(2,2)],
            1 : [P(1,0), P(1,1), P(1,2), P(2,0)],
            2 : [P(0,0), P(0,1), P(1,1), P(2,1)],
            3 : [P(0,2), P(1,0), P(1,1), P(1,2)]
        }
        self.move(0, 3)

class JBlock(Blocks):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0 : [P(0,1), P(1,1), P(2,1), P(2,0)],
            1 : [P(0,0), P(1,0), P(1,1), P(1,2)],
            2 : [P(0,1), P(0,2), P(1,1), P(2,1)],
            3 : [P(1,0), P(1,1), P(1,2), P(2,2)]
        }
        self.move(0, 4)

class IBlock(Blocks):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0 : [P(0,1), P(1,1), P(2,1), P(3,1)],
            1 : [P(1,0), P(1,1), P(1,2), P(1,3)]
        }
        self.move(0, 3)

class TBlock(Blocks):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0 : [P(0,1), P(1,0), P(1,1), P(1,2)],
            1 : [P(0,1), P(1,1), P(1,2), P(2,1)],
            2 : [P(1,0), P(1,1), P(1,2), P(2,1)],
            3 : [P(1,0), P(0,1), P(1,1), P(2,1)]
        }
        self.move(0, 3)

class SquareBlock(Blocks):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0 : [P(0,0), P(0,1), P(1,0), P(1,1)]
        }
        self.move(0, 4)

class HBlock(Blocks):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0 : [P(0,1), P(1,1), P(1,2), P(2,2)],
            1 : [P(1,1), P(1,2), P(2,0), P(2,1)]
        }
        self.move(0, 3)

class HInvertBlock(Blocks):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0 : [P(0,1), P(1,0), P(1,1), P(2,0)],
            1 : [P(1,0), P(1,1), P(2,1), P(2,2)]
        }
        self.move(0, 4)

class ZBlock(Blocks):
    def __init__(self):
        super().__init__(id = 8)
        self.cells = {
            0 : [P(0,0), P(0,1), P(1,1), P(1,2)],
            1 : [P(0,1), P(1,0), P(1,1), P(2,0)]
        }
        self.move(0, 3)

class SBlock(Blocks):
    def __init__(self):
        super().__init__(id = 9)
        self.cells = {
            0 : [P(0,1), P(0,2), P(1,0), P(1,1)],
            1 : [P(0,0), P(1,0), P(1,1), P(2,1)]
        }
        self.move(0, 3)

class UBlock(Blocks):
    def __init__(self):
        super().__init__(id = 10)
        self.cells = {
            0 : [P(0,0), P(0,2), P(1,0), P(1,1), P(1,2)],
            1 : [P(0,1), P(0,2), P(1,1), P(2,1), P(2,2)],
            2 : [P(1,0), P(1,1), P(1,2), P(2,0), P(2,2)],
            3 : [P(0,0), P(0,1), P(1,1), P(2,0), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)

class TridentBlock(Blocks):
    """The Tridentblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 11
        super().__init__(id = 11)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,0), P(0,2), P(1,0), P(1,1), P(1,2), P(2,1)],
            1 : [P(0,1), P(0,2), P(1,0), P(1,1), P(2,1), P(2,2)],
            2 : [P(0,1), P(1,0), P(1,1), P(1,2), P(2,0), P(2,2)],
            3 : [P(0,0), P(0,1), P(1,1), P(1,2), P(2,0), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class CrossBlock(Blocks):
    """The Crossblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 12
        super().__init__(id = 12)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,1), P(1,0), P(1,1), P(1,2), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class HlongBlock(Blocks):
    """The Hlongblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 13
        super().__init__(id = 13)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,0), P(1,0), P(1,1), P(1,2), P(2,2)],
            1 : [P(0,1), P(0,2), P(1,1), P(2,0), P(2,1)]
        }
        # initital position of the block on the screen
        self.move(0, 3)


class HIlongBlock(Blocks):
    """The Hinvertedlongblock tetramino"""
    def __init__(self):
        # inherit from base Block class and have the id set to 14
        super().__init__(id = 14)
        # dictionary holding each rotation for the block
        self.cells = {
            0 : [P(0,2), P(1,0), P(1,1), P(1,2), P(2,0)],
            1 : [P(0,0), P(0,1), P(1,1), P(2,1), P(2,2)]
        }
        # initital position of the block on the screen
        self.move(0, 3)
