import pygame
import math
from state import State
from typing import List, Optional

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
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

GRAVITY = 1

class Entity(pygame.sprite.Sprite):
    def __init__(self,
                 states: List[State] = [State.EMPTY],
                 resDir: str = None):
        super().__init__()
        self.states = states
        self.resDir = resDir

        self.index = 0
        self.x_speed = 0
        self.y_speed = 0
        self.tick = 0
        self.direction = True
        self.grounded = False

        try:
            self.loadImages()

            self.state = states[0]
            self.images = self.imgDict[self.state]

            self.surf = self.images[self.index]
            self.rect = self.surf.get_rect()
        except:
            pass
            # print("unable to fetch assets")

    def loadImages(self):
        self.imgDict = {}

        for s in self.states:
            load = False
            n = 0
            imgList = []
            while not load:
                try:
                    surf = pygame.image.load(
                    f'{self.resDir}/{s}_{n}.png').convert()
                    surf.set_colorkey((255, 255, 255), RLEACCEL)
                    imgList.append(surf)
                    n += 1
                except:
                    load = True
            self.imgDict[s] = imgList

    # def checkIndex(self):
    #     self.tick += 1
    #     interval = {"stand1": 60, "walk1": 10, "jump": 10}
    #     if self.tick == interval[self.state]:
    #         self.index += 1
    #         self.tick = 0
    #     if self.index >= len(self.images):
    #         self.index = 0

    # Move the sprite based on user keypresses
    def update(self, pressed_keys=[]):
        pass
