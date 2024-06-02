import pygame
from grid import Grid
from tetraminoes import *

class Game:

    def __init__(self):
        self.grid = Grid()
        self.current_block = self.generate_block()
        self.next_blocks = [self.generate_block() for _ in range(3)]
        self.score = 0
        self.game_over = False
        self.lives = 3

    def drop_block_at_mouse_position(self):
        if self.current_block:
            grid_x = self.mouse_x // self.cell_size
            grid_y = self.mouse_y // self.cell_size

            self.current_block.move(grid_y - self.current_block.y_offset, grid_x - self.current_block.x_offset)

    def update_block_position_with_mouse(self):
        if self.current_block

    def generate_block(self):
        return random.choice([LBlock(), JBlock(), IBlock(), TBlock(), SquareBlock(), HBlock(), HInvertedBlock(), ZBlock(), SBlock(), UBlock(), TridentBlock(), CrossBlock(), HlongBlock(), HIlongBlock()])
    
    def draw(self, screen):
        self.grid.draw_grid(screen)
        self.current_block.draw_block(screen, 0, 0)

    def mouse_movement(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mose.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            drop_block_at_mouse_position()

        elif event.type == pygame.MOUSEMOTION:
            update_block_at_mouse_position()

    def upfdate(self):

    def game_loop(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.typr == pygame.QUIT:
                    self.game_over  = True
                self.handle_mouse_movement(event)
            self.update()
            self.draw(screen)
            pygame.display.update()