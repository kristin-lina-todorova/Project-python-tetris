from correct_colors import Colors
import pygame

class Grid:
    """A class Grid to display the area for the blocks"""
    def __init__(self):
        self.rows = 9  # number of rows
        self.columns = 9  # number of columns
        self.tile_size = 30  # the size of each grid cell
        # set each area of the grid to be 0 which means empty
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        # get the list of colors
        self.colors = (0, 0, 0)

    def draw_grid(self, screen):
        """Draws the grid to the screen
        Args:
            screen (obj): screen display
        """
        # loop through each rows and columns and change the cell value according to the block dropped
        for ro in range(self.rows):
            for col in range(self.columns):
                # cell_value will change according to the number in the grid
                cell_value = self.grid[ro][col]
                # col is the x axis, ro is the y axis, tile_size is the width and height
                x = col * self.tile_size + 1
                y = ro * self.tile_size + 1
                width_height = self.tile_size - 1
                cell_rect = pygame.Rect(x, y, width_height, width_height)
                # color is changed according to the number in cell_value
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
