# game.py

import sys
import pygame
from tetraminoes import *
from grid import Grid

class Game:
    """Game class to run the game"""

    def __init__(self):
        """Initialization of the Game class"""
        self.grid = Grid()
        self.current_block = None
        self.next_block = None
        self.game_over = False
        self.score = 0
        self.screen = pygame.display.set_mode((500, 600))

    def draw(self, screen):
        """Draw the game elements on the screen"""
        screen.fill((0, 0, 0))  # Fill the screen with black color

        # Draw the grid
        self.grid.draw_grid(screen)

        # Draw the current block
        if self.current_block:
            self.current_block.draw_block(screen)
        else:
            print("Current block is None")

        # Draw the next block
        if self.next_block:
            self.next_block.draw_block(screen, offset_x=200, offset_y=50)  # Adjust the offset as needed
        else:
            print("Next block is None")

        # Draw the score
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        screen.blit(score_text, (50, 50))  # Adjust the position as needed

        # Update the display
        pygame.display.flip()

    def keypress(self, update):
        """Listens for keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == update and not self.game_over:
                self.move_down()

    def move_down(self):
        """Move the current block down"""
        if self.current_block:
            if self.grid.can_move_down(self.current_block):
                self.current_block.move(1, 0)
            else:
                self.grid.add_block_to_grid(self.current_block)
                self.current_block = self.next_block
                self.next_block = self.generate_block()
                rows_cleared = self.grid.clear_rows()
                self.score += rows_cleared * 10

    def generate_block(self):
        """Generate a new random block"""
        import random
        tetromino_types = [IBlock, JBlock, LBlock, SBlock, TBlock, ZBlock]
        random_tetromino = random.choice(tetromino_types)
        print("Generating new block:", random_tetromino.__name__)
        return random_tetromino()

    def move_block_left(self):
        """Move the current block to the left"""
        if self.current_block:
            self.current_block.move(0, -1)

    def move_block_right(self):
        """Move the current block to the right"""
        if self.current_block:
            self.current_block.move(0, 1)

    def rotate_block(self):
        """Rotate the current block"""
        if self.current_block:
            self.current_block.rotation()

    def current_block_position(self):
        """Return the position of the current block"""
        if self.current_block:
            return self.current_block.position()

    def start(self):
        """Start the game"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.key.set_repeat(250, 25)

        UPDATE = pygame.USEREVENT
        pygame.time.set_timer(UPDATE, 300)

        while not self.game_over:
            self.keypress(UPDATE)
            self.draw(self.screen)
            clock.tick(5)

if __name__ == "__main__":
    game = Game()
    game.start()
