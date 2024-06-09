# main.py

import pygame
from colors import Colors
from disp import Display
from game import Game
from grid import Grid

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

        # handle keyboard events for block movements
        if event.type == pygame.KEYDOWN and not game.game_over:
            if event.key == pygame.K_LEFT:
                game.move_block_left()
            elif event.key == pygame.K_RIGHT:
                game.move_block_right()
            elif event.key == pygame.K_DOWN:
                game.move_down()
            elif event.key == pygame.K_UP:
                game.rotate_block()

    screen.fill(background)

    # draw grid
    grid.draw_grid(screen)  # Draw the game grid

    # draw current block
    if game.current_block:
        game.current_block.draw_block(screen, 0, 0)

    # draw next block
    if game.next_block:
        game.next_block.draw_block(screen, 320, 160)

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
