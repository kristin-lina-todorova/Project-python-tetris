import pygame
from colors import Colors
from pos import BlockPosition as P

class Blocks:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 50
        self.rot = 0
        self.colors = Colors().get_color()
        self.y_offset = 0
        self.x_offset = 0

def move(self, y, x):
    self.y_offset += y
    self.x_offset += x

def cell_pos(self):
    tiles = self.cells[self.rot]
    new_pos = []
    for i in tiles:
        i = P(i.y + self.y_offset, i.x +self.x_offset)
        new_pos.append(i)
    return new_pos

def draw_block(self, screen, offset_x, offset_y):
    tiles = self.cell_pos()
    for tile in tiles:
        by = offset_y + tile.y * self.cell_size
        bx = offset_x + tile.x * self.cell_size
        width_height = self.cell_size - 1
        tile_rect = pygame.Rect(bx, by, width_height, width_height)
        pygame.draw.rect(screen, self.colors[self.id], tile_rect)

def rotation(self):
    length = len(self.cells)
    self.rot += 1
    if self.rot == length or self.rot < 0:
        self.rot = 0

def un_rotate(self):
    length = len(self.cells)
    self.rot -= 1
    if self.rot < 0:
        self.rot = length - 1