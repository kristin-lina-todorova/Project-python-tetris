import pygame
from grid import Grid
from game import Game

pygame.init()

screen_width, screen_height = 500, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetratios")

title_font = pygame.font.Font(None, 40)
intro_font = pygame.font.Font(None, 30)

clock = pygame.time.Clock*()
game = Game()

while not game.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over = True
        game.handle_mouse_movement(event)
    game.update()

    screen.fill((black))
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
