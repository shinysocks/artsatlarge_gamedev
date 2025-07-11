'''
TEMPLATE

Use this as a starting point for new creations!

Noah Dinan 2025
'''

import pygame
from lib.lib import Animation, Sprite, Text, Direction, Position, initialize, set_background_color, update, get_mouse_pos, mouse_clicked, quit, wait, check_collision, is_key_pressed

# Pygame keys documentation here: https://www.pygame.org/docs/ref/key.html

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
TITLE = "CHANGE ME!"

initialize(SCREEN_WIDTH, SCREEN_HEIGHT, "CHANGE ME!")

# Create some animations
# animation = Animation("spritesheet.png", fps, columns, rows, number_of_frames)

# Make some sprites!
# sprite = Sprite(animation, Position(0, 0), size=(150, 150))


# set color to green
set_background_color(0, 255, 0)


while True:
    # Write your game logic here!


    # if sprite.clicked():
    #     sprite.move(Direction.LEFT)


    # Don't remove
    update()
