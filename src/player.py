import pygame
import math
from entity import Entity
from state import State

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_f,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

GRAVITY = 1

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def checkIndex(self):
        self.tick += 1
        interval = {State.STAND: 60, State.WALK_1: 10, State.JUMP: 10}
        if self.tick == interval[self.state]:
            self.index += 1
            self.tick = 0
        if self.index >= len(self.images):
            self.index = 0

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            # self.x_speed = 
            self.rect.move_ip(-5, 0)
            if self.state != State.WALK_1 and self.grounded:
                self.state = State.WALK_1
                self.tick = 0
                self.index = 0
            self.direction = False
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            if self.state != State.WALK_1 and self.grounded:
                self.state = State.WALK_1
                self.tick = 0
                self.index = 0
            self.direction = True
        if not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT]:
            if self.state != State.STAND and self.grounded:
                self.state = State.STAND
                self.tick = 0
                self.index = 0
        if pressed_keys[K_UP]:
            if self.grounded:
                self.y_speed = -20
                self.grounded = False

        self.rect.move_ip(0, self.y_speed+GRAVITY)

        if not self.grounded:
            self.y_speed += GRAVITY

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.grounded = True

        if pressed_keys[K_f]:
            pass


        if not self.grounded and self.state != State.JUMP:
            self.state = State.JUMP
            self.tick = 0
            self.index = 0
        self.checkIndex()
        self.images = self.imgDict[self.state]

        if not self.direction:
            self.surf = self.images[self.index]
        else:
            self.surf = pygame.transform.flip(self.images[self.index], True, False)