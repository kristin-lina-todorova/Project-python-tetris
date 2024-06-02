import pygame
from colors import Colors

class Grid:

    def __init__(self):
        self.x = 10
        self.y = 20
        self.square_size = 30
        self.grid = []
        for i in range(self.x):
            row = []
            for j in range(self.y):
                row.append(0)
            self.grid.append(row)
        self.color = Colors.get_color()

    def draw_grid(self, screen):
        for row in range(self.rows):
            for col in range(self.coumns):
                cell_value = self.grid[row][col]
                x = col * self.tile_size + 1
                y = row * self.tile_size + 1
                width_height = self.tile_size - 1
                cell_rect = pygame.Rect(x, y, width_height, width_height)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def grid_check(self, y, x):
        if 0 <= y < self.rows and 0 <= x < self.columns:
            return True
        return False
    
    def empty_grid(self, y, x):
        if self.grid[y][x] == 0:
            return True
        return False
    
    def full_row(self, y):
        for x in range(self.columns):
            if self.grid[y][x] == 0:
                return False
        return True
    
    def clear(self, y):
        for x in range(self.columns):
            self.grid[y][x] == 0

    def move_row(self, y, num_row):
        for x in range(self.columns):
            self.grid[y + num_row][x] = self.grid[y][x]
            self.grid[y][x] = 0

    def clear_row(self):
        complete = 0
        for y in range (self.rows - 1, 0, -1):
            if self.full_row(y):
                self.clear(y)
                complete += 1
            elif complete > 0:
                self.move_row(y, complete)
        return complete
    
    def grid_reset(self):
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

