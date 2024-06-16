import pygame
from correct_tetraminoes import Blocks
from correct_colors import Colors

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 600))
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(10)] for _ in range(20)]
        self.current_block = self.generate_new_block()  # Initialize the first block
        self.next_block = self.generate_new_block()  # Initialize the next block
        self.block_x = 3
        self.block_y = 0  # Position the block at the top of the grid
        self.game_over = False
        self.score = 0
        self.dragging = False

    def generate_new_block(self):
        return Blocks(1)  # Replace with logic to generate a random block if needed

    def draw(self):
        self.screen.fill(Colors.screen_background)
        self.draw_grid()
        if self.current_block:
            print(f"Drawing block at {self.block_x}, {self.block_y}")
            self.current_block.draw_block(self.screen, self.block_x, self.block_y)
        pygame.display.flip()

    def draw_grid(self):
        for y in range(20):
            for x in range(10):
                cell_value = self.grid[y][x]
                color = Colors.get_color()[cell_value]
                pygame.draw.rect(self.screen, color, pygame.Rect(x * 30, y * 30, 29, 29), 1)

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
            self.update()
            self.draw()
            self.clock.tick(10)

    def update(self):
        # Move the block down
        if not self.check_collision(self.block_x, self.block_y + 1):
            self.block_y += 1
        else:
            self.place_block()
            self.current_block = self.next_block
            self.next_block = self.generate_new_block()
            self.block_x = 3
            self.block_y = 0
            # Check if the new block can be placed; if not, game over
            if not self.check_collision(self.block_x, self.block_y):
                self.game_over = True

    def place_block(self):
        for tile in self.current_block.cell_pos():
            self.grid[tile.y + self.block_y][tile.x + self.block_x] = self.current_block.id

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
        for tile in self.current_block.cell_pos():
            if (
                tile.x + x < 0 or tile.x + x >= 10 or
                tile.y + y < 0 or tile.y + y >= 20 or
                self.grid[tile.y + y][tile.x + x] != 0
            ):
                return False
        return True

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
