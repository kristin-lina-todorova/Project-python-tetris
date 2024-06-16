# tetra.py
import pygame
from correct_colors import Colors
from correct_pos import BlockPosition as P

class Blocks:
    """A base class Blocks that each block/tetramino will inherit from"""
    def __init__(self, id):
        """Initialization of Block class
        Args:
            id (int): id of the block
        """
        self.id = id
        self.cells = {0: []}  # Initialize with an empty list for rotation 0
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

    def draw_block(self, screen, block_x, block_y):
        """Draw the block on the screen
        Args:
            screen (obj): screen object
            block_x (int): x position of the block
            block_y (int): y position of the block
        """
        # Get the position of each cell of the current block
        tiles = self.cell_pos()
        for tile in tiles:
            # bx represents the column, by the row
            by = (tile.y + block_y) * self.cell_size
            bx = (tile.x + block_x) * self.cell_size
            width_height = self.cell_size - 1
            tile_rect = pygame.Rect(bx, by, width_height, width_height)
            # Draw the block to the screen
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

    def get_rect(self, block_x, block_y):
        """Get the rectangle enclosing the block
        Args:
            block_x (int): x position of the block
            block_y (int): y position of the block
        Returns:
            pygame.Rect: Rectangle enclosing the block
        """
        tiles = self.cell_pos()
        min_x = min(tile.x for tile in tiles) + block_x
        max_x = max(tile.x for tile in tiles) + block_x
        min_y = min(tile.y for tile in tiles) + block_y
        max_y = max(tile.y for tile in tiles) + block_y
        rect_x = min_x * self.cell_size
        rect_y = min_y * self.cell_size
        rect_width = (max_x - min_x + 1) * self.cell_size
        rect_height = (max_y - min_y + 1) * self.cell_size
        return pygame.Rect(rect_x, rect_y, rect_width, rect_height)
