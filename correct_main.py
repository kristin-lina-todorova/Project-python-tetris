import pygame
from correct_colors import Colors
from correct_disp import Display
from correct_game import Game
from correct_grid import Grid

pygame.init()

background = Colors.screen_background

screen = pygame.display.set_mode((500, 600))

pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

display = Display(screen)

grid = Grid()

UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.start_drag(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            game.stop_drag()
        elif event.type == pygame.MOUSEMOTION:
            game.drag_block(event.pos)

    screen.fill(background)

    grid.draw_grid(screen)

    if game.current_block:
        game.current_block.draw_block(screen, game.block_x, game.block_y)

    score_text = pygame.font.Font(None, 40).render("Score: " + str(game.score), True, Colors.grid_color)
    screen.blit(score_text, (350, 20))

    if game.game_over:
        game_over_font = pygame.font.Font(None, 60)
        game_over_text = game_over_font.render("GAME OVER", True, Colors.red)
        screen.blit(game_over_text, (100, 250))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        quit()

    pygame.display.update()
    clock.tick(60)
