'''
MOVEMENT

Simple movement demo

Noah Dinan 2025
'''

# Scary imports (ignore these!)
import pygame
from lib.lib import BLUE, GREEN, RED, WHITE, BLACK, Animation, Sprite, Text, Direction, Position, initialize, set_background_color, update, get_mouse_pos, mouse_clicked, get_keys, quit, wait, check_collision

# Pygame keys documentation here: https://www.pygame.org/docs/ref/key.html

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

initialize(SCREEN_WIDTH, SCREEN_HEIGHT, "Simple Movement Demo!")

animation = Animation("Heart_Shocked.png", fps=4, columns=1, rows=2, number_of_frames=2)

heart = Sprite(animation, Position(0, 0), size=(150, 150))

while True:

    # iterate through each key
    for key in get_keys():
        # move the heart based on arrow keys
        if key is pygame.K_LEFT:
            heart.move(Direction.LEFT)
        if key is pygame.K_RIGHT:
            heart.move(Direction.RIGHT)
        if key is pygame.K_UP:
            heart.move(Direction.UP)
        if key is pygame.K_DOWN:
            heart.move(Direction.DOWN)

    # do not remove
    update()
