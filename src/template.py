'''
TEMPLATE

Use this as a starting point for new creations!

Noah Dinan 2025
'''

import pygame
from lib import BLUE, GREEN, RED, WHITE, BLACK, Animation, Sprite, Text, Direction, Position, initialize, set_background_color, update, get_mouse_pos, mouse_clicked, get_keys, quit, wait

# Pygame keys documentation here: https://www.pygame.org/docs/ref/key.html

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

initialize(SCREEN_WIDTH, SCREEN_HEIGHT, "CHANGE ME!")

# Create some animations
# animation = Animation("spritesheet.png", fps, columns, rows, number_of_frames)

# Make some sprites!
# sprite = Sprite(animation, Position(0, 0), size=(150, 150))


set_background_color(GREEN)


while True:
    # Write your game logic here!


    # if sprite.clicked():
    #     sprite.move(Direction.LEFT)
    # else:
    #     sprite.stop()


    # Don't remove
    update()
