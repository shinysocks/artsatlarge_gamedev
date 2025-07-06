'''
TEMPLATE

Use this as a starting point for new creations!

Noah Dinan 2025
'''

import pygame
from lib.lib import BLUE, GREEN, RED, WHITE, BLACK, Animation, Sprite, Text, Direction, Position, initialize, set_background_color, update, get_mouse_pos, mouse_clicked, get_keys, quit, wait, check_collision

# Pygame keys documentation here: https://www.pygame.org/docs/ref/key.html

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
TITLE = "ajsekajdskabkdsakd k"

initialize(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)

# Create some animations
potato_default = Animation("potato.png", fps=9, columns=3, rows=4, number_of_frames=11)

# Make some sprites!
potato = Sprite(potato_default, Position(200, 200), size=(150, 150))

custom_color = (240, 230, 100)

set_background_color(custom_color)

while True:
    w = potato.get_width() + 1
    h = potato.get_height() + 1

    potato.set_size( (w, h) )

    # Write your game logic here!


    # if sprite.clicked():
    #     sprite.move(Direction.LEFT)
    # else:
    #     sprite.stop()


    # Don't remove
    update()
