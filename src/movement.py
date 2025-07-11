'''
MOVEMENT

Simple movement demo

Noah Dinan 2025
'''

# Scary imports (ignore these!)
import pygame
from lib.lib import Animation, Sprite, Text, Direction, Position, initialize, set_background_color, update, get_mouse_pos, mouse_clicked, quit, wait, check_collision, is_key_pressed

# Pygame keys documentation here: https://www.pygame.org/docs/ref/key.html

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

initialize(SCREEN_WIDTH, SCREEN_HEIGHT, "Simple Movement Demo!")

animation = Animation("Heart_Shocked.png", fps=4, columns=1, rows=2, number_of_frames=2)

heart = Sprite(animation, Position(0, 0), size=(150, 150))

while True:

    # move the heart based on arrow keys
    if is_key_pressed(pygame.K_LEFT):
        heart.move(Direction.LEFT, speed=10)
    if is_key_pressed(pygame.K_RIGHT):
        heart.move(Direction.RIGHT, speed=2)
    if is_key_pressed(pygame.K_UP):
        heart.move(Direction.UP, speed=2)
    if is_key_pressed(pygame.K_DOWN):
        heart.move(Direction.DOWN, speed=2)

    # do not remove
    update()
