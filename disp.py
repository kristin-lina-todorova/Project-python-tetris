import pygame

class Display:
    def __init__(self, screen):
        self.screen = screen

    def display(self, text, position):
        self.screen.blit(text, position)
