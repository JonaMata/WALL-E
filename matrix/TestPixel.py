import pygame


class TestPixel(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.color = (0, 0, 0)
        self.surf = pygame.Surface((size, size))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center=(pos[0] * size + size / 2, pos[1] * size + size / 2))

    def set_color(self, color):
        self.color = color

    def display(self, surface):
        self.surf.fill(self.color)
        surface.blit(self.surf, self.rect)
