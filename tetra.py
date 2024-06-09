import pygame
from colors import Colors
from pos import BlockPosition as P

class Blocks:
    """A base class Blocks that each block/tetramino will inherit from"""
    def __init__(self, id):
        """Initialization of Block class
        Args:
            id (int): id of the block
        """
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rot = 0
        self.colors = Colors.get_color()
        self.y_offset = 0
        self.x_offset = 0

    def move(self, y, x):
        """Move the block/tetramino
        Args:
            y (int): y axis (row)
            x (int): x axis (column)
        """
        # Increase the offsets according to the numbers obtained from x and y
        self.y_offset += y
        self.x_offset += x

    def cell_pos(self):
        """Get the position of each cell of the current block/tetramino
        Returns:
            new (list): a list of the position for the current block
        """
        # Get the block according to the rotation position
        tiles = self.cells[self.rot]
        new_pos = []
        for ti in tiles:
            ti = P(ti.y + self.y_offset, ti.x + self.x_offset)
            new_pos.append(ti)
        return new_pos

    def draw_block(self, screen):
        """Draw the block on the screen
        Args:
            screen (obj): screen object
        """
        # Get the position of each cell of the current block
        tiles = self.cell_pos()
        for tile in tiles:
            # bx represents the column, by the row
            by = tile.y * self.cell_size
            bx = tile.x * self.cell_size
            width_height = self.cell_size - 1
            tile_rect = pygame.Rect(bx, by, width_height, width_height)
            # Draw the block to the screen
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
