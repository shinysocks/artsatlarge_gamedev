'''
GROWING CAT

Click on the cat!

Noah Dinan 2025
'''

import pygame

from lib.lib import BLUE, GREEN, RED, WHITE, BLACK, Animation, Sprite, Text, Direction, Position, initialize, set_background_color, update, get_mouse_pos, mouse_clicked, quit, wait, check_collision, is_key_pressed

# Pygame keys documentation here: https://www.pygame.org/docs/ref/key.html

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SILLY_COLOR = (230, 100, 35)
CENTER_POS = Position(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# initialize the game window
initialize(SCREEN_WIDTH, SCREEN_HEIGHT, "Click on the cat!")


# You can create any number of animations based on spritesheets exported from piskel!
heart_default = Animation("Heart_Default.png",
                          fps=7, # how many frames per second do you want your animation to play at?
                          columns=2, # how many columns in spritesheet
                          rows=2, # how many rows in spritesheet
                          number_of_frames=4) # how many frames are in your animation?

tan_cat = Animation("tan_cat.png", fps=6, columns=2, rows=2, number_of_frames=4)

tan_cat_shocked = Animation("tan_cat_shocked.png", fps=7, columns=3, rows=3, number_of_frames=7)

# sprites can be created with an animation, position, and size
cat = Sprite(tan_cat, CENTER_POS, size=(150, 150))

heart = Sprite(heart_default, get_mouse_pos(), size=(50, 50))

# create a special Text sprite
text = Text(color=WHITE, position=Position(10, 10))

# set our background color to black
set_background_color(SILLY_COLOR)

# GAME LOOP
while True:
    # set the position of the heart to follow mouse position
    new_heart_pos = get_mouse_pos()
    new_heart_pos.x += 50 # offset from the mouse position
    new_heart_pos.y -= 50

    heart.set_pos(pos=new_heart_pos)

    # if mouse hovers over cat, set animation to shocked
    if cat.hovered():
        cat.set_anim(tan_cat_shocked)
    else:
        cat.set_anim(tan_cat)

    if cat.clicked():
        # increase the size of the cat
        cat.set_size( (cat.get_width() + 1, cat.get_height() + 1) )
        cat.set_pos(SCREEN_WIDTH / 2, cat.get_pos().y)

        text.set_color(RED)
        text.set_text("You're pressing on the cat!")
    else:
        text.set_text("")

    # wait(seconds) will return true after seconds have passed
    if wait(5):
        print("5 seconds have passed")
    # you can use this to create delays

    # do not remove
    update()

