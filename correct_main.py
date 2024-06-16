# main.py

import pygame
from correct_colors import Colors
from correct_disp import Display
from correct_game import Game
from correct_grid import Grid

# pygame initialization
pygame.init()

# background color
background = Colors.screen_background

# set up screen display
screen = pygame.display.set_mode((500, 600))

# game caption
pygame.display.set_caption("Tetris")

# clock for controlling the frame rate
clock = pygame.time.Clock()

# instance of the Game class
game = Game()

# instance of the Display class
display = Display(screen)

# instance of the Grid class
grid = Grid()

# make game update itself every 300 milliseconds
UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 300)

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # handle mouse events for block dragging
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.start_drag(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            game.stop_drag()
        elif event.type == pygame.MOUSEMOTION:
            game.drag_block(event.pos)

    screen.fill(background)

    # draw grid
    grid.draw_grid(screen)  # Draw the game grid

    # draw current block
    if game.current_block:
        game.current_block.draw_block(screen, game.block_x, game.block_y)

    # draw score
    score_text = pygame.font.Font(None, 40).render("Score: " + str(game.score), True, Colors.grid_color)
    screen.blit(score_text, (350, 20))

    # Check for game over
    if game.game_over:
        # Display game over message
        game_over_font = pygame.font.Font(None, 60)
        game_over_text = game_over_font.render("GAME OVER", True, Colors.red)
        screen.blit(game_over_text, (100, 250))
        pygame.display.update()
        pygame.time.wait(2000)  # Wait for 2 seconds before quitting
        pygame.quit()
        quit()

    # update screen
    pygame.display.update()
    clock.tick(60)
