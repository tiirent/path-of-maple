import random
import pygame
from threading import Timer
from entity import Entity
from state import State

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

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                # random.randint(0, SCREEN_HEIGHT),
                SCREEN_HEIGHT-(self.rect.height/2),
            )
        )
        self.speed = random.randint(5, 20)
        self.state = State.WALK

    def checkIndex(self):
        self.tick += 1
        interval = {State.WALK: 20, State.DEAD: 15}
        if self.tick == interval[self.state]:
            self.index += 1
            self.tick = 0
        if self.index >= len(self.images):
            self.index = 0

    def die(self):
        if self.state != State.DEAD:
            self.state = State.DEAD
            t = Timer(1, self.kill)
            t.start()

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.checkIndex()
        self.images = self.imgDict[self.state]
        self.surf = self.images[self.index]
        if self.state != State.DEAD:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()