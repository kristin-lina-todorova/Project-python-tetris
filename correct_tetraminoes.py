from correct_pos import BlockPosition as P
from correct_colors import Colors
import pygame

class Blocks:
    def __init__(self, block_id):
        self.id = block_id
        self.cells = self.get_block_cells(block_id)
        self.cell_size = 30
        self.rot = 0
        self.colors = Colors.get_color()
        self.y_offset = 0
        self.x_offset = 3

    def get_block_cells(self, block_id):
        blocks = {
            1: {
                0: [P(0, 0), P(0, 1), P(0, 2), P(1, 0)],     # LBlock
                1: [P(0, 0), P(1, 0), P(2, 0), P(2, 1)],
                2: [P(0, 2), P(1, 0), P(1, 1), P(1, 2)],
                3: [P(0, 0), P(0, 1), P(1, 1), P(2, 1)]
            },
            2: {
                0: [P(0, 1), P(1, 1), P(2, 1), P(2, 0)],     # JBlock
                1: [P(0, 0), P(1, 0), P(1, 1), P(1, 2)],
                2: [P(0, 1), P(0, 2), P(1, 1), P(2, 1)],
                3: [P(1, 0), P(1, 1), P(1, 2), P(2, 2)]
            },
            3: {
                0: [P(0, 1), P(1, 1), P(2, 1), P(3, 1)],     # IBlock
                1: [P(1, 0), P(1, 1), P(1, 2), P(1, 3)]
            },
            4: {
                0: [P(0, 1), P(1, 0), P(1, 1), P(1, 2)],     # TBlock
                1: [P(0, 1), P(1, 1), P(1, 2), P(2, 1)],
                2: [P(1, 0), P(1, 1), P(1, 2), P(2, 1)],
                3: [P(1, 0), P(0, 1), P(1, 1), P(2, 1)]
            },
            5: {
                0: [P(0, 1), P(0, 2), P(1, 0), P(1, 1)],     # SBlock
                1: [P(0, 0), P(1, 0), P(1, 1), P(2, 1)]
            },
            6: {
                0: [P(0, 0), P(0, 1), P(1, 1), P(1, 2)],     # ZBlock
                1: [P(0, 1), P(1, 0), P(1, 1), P(2, 0)]
            },
            7: {
                0: [P(0, 0), P(0, 1), P(1, 0), P(1, 1)]      # OBlock
            },
            8: {
                0: [P(0, 0), P(0, 1), P(0, 2), P(1, 0), P(1, 2)], # PyramideBlock
                1: [P(0, 0), P(1, 0), P(1, 1), P(2, 1), P(2, 2)],
                2: [P(1, 0), P(1, 2), P(2, 0), P(2, 1), P(2, 2)],
                3: [P(0, 0), P(0, 1), P(1, 1), P(2, 1), P(2, 2)]
            },
            9: {
                0: [P(0, 1), P(1, 0), P(1, 1), P(1, 2), P(2, 1)]  # PlusBlock
            },
            10: {
                0: [P(0, 0), P(0, 1), P(0, 2), P(0, 3), P(0, 4), P(1, 2), P(2, 2)], # ExtraBlock
                1: [P(0, 2), P(1, 0), P(1, 1), P(1, 2), P(1, 3), P(1, 4), P(2, 2)]
            }
        }
        return blocks.get(block_id, {})

    def move(self, y, x):
        self.y_offset += y
        self.x_offset += x

    def cell_pos(self):
        tiles = self.cells[self.rot]
        new_pos = []
        for ti in tiles:
            ti = P(ti.y + self.y_offset, ti.x + self.x_offset)
            new_pos.append(ti)
        return new_pos

    def draw_block(self, screen, block_x, block_y):
        tiles = self.cell_pos()
        for tile in tiles:
            print(f"Drawing tile at {tile.x}, {tile.y}")  # Debugging statement
            by = (tile.y + block_y) * self.cell_size
            bx = (tile.x + block_x) * self.cell_size
            width_height = self.cell_size - 1
            tile_rect = pygame.Rect(bx, by, width_height, width_height)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

    def get_rect(self, block_x, block_y):
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
