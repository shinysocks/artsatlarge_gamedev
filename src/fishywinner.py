'''
FISHY WINNER

Race the fish to the finishline!

Daisy DiCarlo 2025
'''

import pygame
from lib.lib import Animation, Sprite, Text, Direction, Position, initialize, set_background_color, update, get_mouse_pos, mouse_clicked, quit, wait, check_collision, is_key_pressed

# Pygame keys documentation here: https://www.pygame.org/docs/ref/key.html

WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
TITLE = "Fishy Winner"

initialize(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)

# Create some animations
swim = Animation("Fishy_Sprite.png", fps=7, columns=1, rows=2, number_of_frames=2)
still = Animation("FISHYDEFS.png", fps=1, columns=1, rows=1, number_of_frames=1)
finishline = Animation("finishline.png", fps=1, columns=1, rows=1, number_of_frames=1)



# Make some sprites!
finish= Sprite(finishline, Position(0, 0), size=(SCREEN_WIDTH, 125))
fishy= Sprite(still, Position(200, 600), size=(150, 150))
text = Text(Position(SCREEN_WIDTH / 4, SCREEN_HEIGHT/2), color=WHITE)
text2 = Text(Position(SCREEN_WIDTH / 4, (SCREEN_HEIGHT/2) + 50),  color=WHITE)

set_background_color(red=35, green=10, blue=120)


while True:
    # Write your game logic here!


    if fishy.clicked():
        fishy.set_anim(swim)
        fishy.move(Direction.UP)
    else:
        fishy.set_anim(still)


    # if fishy hits finish line, WIN!
    if check_collision(fishy, finish):
        text.set_words("FISHY WINNER")
        text2.set_words("FISHY DINNER!")
        

    # Don't remove
    update()
