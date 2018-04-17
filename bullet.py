import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.ship = ship
        self.rect = pygame.Rect(0, 0, self.ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top
        self.rect.centery = self.ship.rect.centery
        self.color = self.ai_settings.bullet_color
        self.speed = self.ai_settings.bullet_speed

    def update(self):
        self.rect.centery -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
