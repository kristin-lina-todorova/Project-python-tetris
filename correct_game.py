# game.py
import pygame
from correct_tetra import Blocks
from correct_colors import Colors

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 600))
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(10)] for _ in range(20)]
        self.block = Blocks(1)  # Initialize a block
        self.block_x = 5
        self.block_y = 21  # Position the block just below the grid
        self.game_over = False
        self.current_block = self.block  # Use current block
        self.next_block = None  # Placeholder for next block
        self.score = 0
        self.dragging = False

    def draw(self):
        self.screen.fill(Colors.screen_background)
        self.draw_grid()
        if self.current_block:
            self.current_block.draw_block(self.screen, self.block_x, self.block_y)
        pygame.display.flip()

    def draw_grid(self):
        for y in range(20):
            for x in range(10):
                pygame.draw.rect(self.screen, Colors.grid_color, pygame.Rect(x * 30, y * 30, 29, 29), 1)

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_drag(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.stop_drag()
                elif event.type == pygame.MOUSEMOTION:
                    self.drag_block(event.pos)
            self.draw()
            self.clock.tick(10)

    def start_drag(self, pos):
        block_rect = self.current_block.get_rect(self.block_x, self.block_y)
        if block_rect.collidepoint(pos):
            self.dragging = True

    def stop_drag(self):
        self.dragging = False

    def drag_block(self, pos):
        if self.dragging:
            self.block_x = pos[0] // 30
            self.block_y = pos[1] // 30

    def check_collision(self, x, y):
        for cy in range(4):
            for cx in range(4):
                if self.block.get_tile(cx, cy) and (x + cx < 0 or x + cx >= 10 or y + cy >= 20 or self.grid[y + cy][x + cx]):
                    return False
        return True

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
