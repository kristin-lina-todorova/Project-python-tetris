import pygame
from colors import Colors

class Display:
    def __init__(self, screen):
        self.screen = screen

    def display(self, text, rect):
        text_surf = pygame.Surface((rect[2], rect[3]))
        text_surf.fill((white))
        text_rect = text_surf.get_rect(center = (rect[2] // 2, rect[3] // 2))
        text_surf.blit(text, text_rect)
        self.screen.blit(text_surf, (rect[0], rect[1]))

