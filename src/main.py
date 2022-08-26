# Simple pygame program

# Import and initialize the pygame library
import pygame
import db
import custom_event
from player import Player
from enemy import Enemy
from state import State
from attack import Attack

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
pygame.time.set_timer(custom_event.ADDENEMY, 1000)

# Make player
player = Player(states=[State.STAND, State.WALK_1, State.JUMP, State.STAB_1], resDir="../res/img/char/vvook")

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
db.all_sprites.add(player)

# Run until the user asks to quit
clock = pygame.time.Clock()
running = True
# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Add a new enemy?
        elif event.type == custom_event.ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy(states=[State.WALK, State.DEAD], resDir="../res/img/enemy/snail")
            db.enemies.add(new_enemy)
            db.all_sprites.add(new_enemy)

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    db.enemies.update()
    db.attacks.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in db.all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    e = pygame.sprite.spritecollideany(player, db.enemies)
    if e:
        # If so, then remove the player and stop the loop
        player.y_speed = -20
        player.grounded = False
        e.die()
    
    e = pygame.sprite.groupcollide(db.attacks, db.enemies, 0, 0)
    for v in list(e.values()):
        for enemy in v:
            enemy.die()

    pygame.display.flip()
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(60)

# Done! Time to quit.
pygame.quit()