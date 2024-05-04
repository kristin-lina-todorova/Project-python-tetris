import pygame
import random

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
ROWS = 20
COLS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tetrominoes
tetrominoes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # J
    [[1, 1, 1], [0, 0, 1]],  # L
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]]  # Z
]

tetromino_colors = [RED, BLUE, GREEN, CYAN, MAGENTA, YELLOW, ORANGE]

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * COLS for _ in range(ROWS)]
        self.current_tetromino = self.get_random_tetromino()
        self.current_tetromino_x = COLS // 2 - len(self.current_tetromino[0]) // 2
        self.current_tetromino_y = 0
        self.score = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1)
                    if event.key == pygame.K_RIGHT:
                        self.move(1)
                    if event.key == pygame.K_DOWN:
                        self.move_down()

            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_tetromino()
            pygame.display.flip()
            self.clock.tick(5)

    def draw_grid(self):
        for y in range(ROWS):
            for x in range(COLS):
                if self.grid[y][x] != 0:
                    pygame.draw.rect(self.screen, tetromino_colors[self.grid[y][x] - 1],
                                     (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, WHITE,
                                     (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_tetromino(self):
        for y in range(len(self.current_tetromino)):
            for x in range(len(self.current_tetromino[y])):
                if self.current_tetromino[y][x] != 0:
                    pygame.draw.rect(self.screen, tetromino_colors[self.current_tetromino[y][x] - 1],
                                     ((self.current_tetromino_x + x) * BLOCK_SIZE,
                                      (self.current_tetromino_y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, WHITE,
                                     ((self.current_tetromino_x + x) * BLOCK_SIZE,
                                      (self.current_tetromino_y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE), 1)

    def move(self, dx):
        if self.check_collision(self.current_tetromino, self.current_tetromino_x + dx, self.current_tetromino_y):
            self.current_tetromino_x += dx

    def move_down(self):
        if self.check_collision(self.current_tetromino, self.current_tetromino_x, self.current_tetromino_y + 1):
            self.current_tetromino_y += 1
        else:
            self.merge_tetromino()
            self.clear_lines()
            self.current_tetromino = self.get_random_tetromino()
            self.current_tetromino_x = COLS // 2 - len(self.current_tetromino[0]) // 2
            self.current_tetromino_y = 0

    def merge_tetromino(self):
        for y in range(len(self.current_tetromino)):
            for x in range(len(self.current_tetromino[y])):
                if self.current_tetromino[y][x] != 0:
                    self.grid[self.current_tetromino_y + y][self.current_tetromino_x + x] = self.current_tetromino[y][x]

    def check_collision(self, tetromino, x, y):
        for y_idx, row in enumerate(tetromino):
            for x_idx, cell in enumerate(row):
                if cell != 0:
                    if not 0 <= x + x_idx < COLS or not 0 <= y + y_idx < ROWS or self.grid[y + y_idx][x + x_idx] != 0:
                        return False
        return True

    def clear_lines(self):
        lines_cleared = 0
        for y in range(ROWS):
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0] * COLS)
                lines_cleared += 1
        self.score += lines_cleared * 100

    def get_random_tetromino(self):
        return random.choice(tetrominoes)

if __name__ == "__main__":
    game = Tetris()
    game.run()
    pygame.quit()
