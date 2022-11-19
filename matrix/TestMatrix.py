import pygame
from pygame.locals import *
from .TestPixel import TestPixel
from .BaseMatrix import BaseMatrix
import sys


class Matrix(BaseMatrix):
    def __init__(self, width, height, pixel_size):
        super().__init__(width, height, pixel_size)

        pygame.init()
        self.surface = pygame.display.set_mode((self.WIDTH * self.PIX_SIZE, self.HEIGHT * self.PIX_SIZE))
        self.pixels = [[TestPixel((x, y), self.PIX_SIZE) for y in range(self.HEIGHT, 0, -1)] for x in range(self.WIDTH)]

    def display(self):
        self.surface.fill((0, 0, 0))
        for column in self.pixels:
            for pixel in column:
                pixel.display(self.surface)
        pygame.display.update()

    def set_pixel(self, x, y, color):
        self.pixels[x][y].set_color(color)

    def run(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        super().run()
