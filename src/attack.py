import random
import pygame
from entity import Entity

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Attack(Entity):
    def __init__(self, x=0, y=0, duration=60, **kwargs):
        super().__init__(**kwargs)
        self.surf = pygame.Surface((75, 150))
        self.surf.set_colorkey((0,0,0))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            x=x, y=y
        )
        self.duration = duration

    def update(self):
        self.duration -= 1
        
        if self.duration == 0:
            self.kill()
        