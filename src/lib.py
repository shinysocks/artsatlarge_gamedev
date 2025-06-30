import pygame
from math import sqrt

FPS = 60

width = 0
height = 0
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
background_color = WHITE
MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN
wait_amount = 0


class Animation():
    def __init__(self, filename: str, fps, columns, rows, number_of_frames, loop=True):
        self.filename = filename
        self.fps = fps
        self.columns = columns
        self.rows = rows
        self.number_of_frames = number_of_frames
        self.loop = loop
        self.frames = self.load()

    def get_frames(self):
        return self.frames

    def get_fps(self):
        return self.fps

    def load(self):
        subsurfaces = []
        try:
            sheet = pygame.image.load("./src/spritesheets_here/" + self.filename).convert_alpha()
            x_offset = int(sheet.get_width() / self.columns)
            y_offset = int(sheet.get_height() / self.rows)
        except pygame.error as message:
            print(f"Unable to load spritesheet image: {self.filename}")
            print(message)
            exit()

        for y in range(self.rows):
            for x in range(self.columns):
                subsurfaces.append(sheet.subsurface(pygame.Rect(x*x_offset, y*y_offset, x_offset, y_offset)))

        return subsurfaces[0:self.number_of_frames]


class Sprite(pygame.sprite.Sprite):
    '''
    Stores an in-game sprite
    '''
    def __init__(self, animation: Animation, position=(0, 0), size=(100, 100)):
        pygame.sprite.Sprite.__init__(self, sprites)
        self.anim = animation
        self.current_frame = 0
        self.rect = self.anim.get_frames()[0].get_rect()
        self.set_size(size)
        self.set_pos(position)

    def set_pos(self, pos):
        x = pos[0]
        y = pos[1]
        adjusted_width = width - (self.rect.width / 2)
        adjusted_height = height - (self.rect.height / 2)
        
        if x > adjusted_width:
            x = adjusted_width
        elif x < self.rect.width / 2:
            x = self.rect.width / 2
        if y > adjusted_height:
            y = adjusted_height
        elif y < self.rect.height / 2:
            y = self.rect.height / 2

        self.rect.x = x - (self.rect.width / 2)
        self.rect.y = y - (self.rect.height / 2)

    def get_pos_y(self):
        return self.rect.y + (self.rect.height / 2)

    def get_pos_x(self):
        return self.rect.x + (self.rect.width / 2)

    def set_pos_x(self, x):
        self.rect.x = x

    def set_pos_y(self, y):
        self.rect.y = y

    def update(self):
        self.current_frame += self.anim.get_fps() / FPS

        if int(self.current_frame) >= len(self.anim.get_frames()):
            self.current_frame = 0

        frame = pygame.transform.scale(self.anim.get_frames()[int(self.current_frame)], self.rect.size)

        window.blit(frame, self.rect)

    def get_size(self):
        return self.rect.size

    def set_anim(self, new_animation: Animation):
        self.anim = new_animation
        pos = (self.get_pos_x(), self.get_pos_y())
        size = self.get_size()
        self.set_pos(pos)
        self.set_size(size)

    def clicked(self):
        return self.hovered() and mouse_clicked()

    def hovered(self):
        return self.rect.collidepoint(get_mouse_pos()) 

    def set_size(self, dimensions):
        if dimensions[0] <= width and dimensions[1] <= height:
            self.rect.size = dimensions

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height


class Text(pygame.sprite.Sprite):
    def __init__(self, words="", position=(), color=BLUE):
        pygame.sprite.Sprite.__init__(self, sprites)
        self.words = words
        self.position = position
        self.color = color
        self.font = pygame.font.Font("src/font.ttf", 50)

    def update(self):
        text = self.font.render(str(self.words), True, self.color)
        window.blit(text, self.position)

    def set_text(self, t):
        self.words = t 

    def set_color(self, c):
        self.color = c


def initialize(w: int, h: int, caption: str):
    '''
    Initialize a game window with specified dimensions and title

    '''
    global window, width, height
    width = w
    height = h
    pygame.init()
    window = pygame.display.set_mode((w, h))
    pygame.display.set_caption(caption)


def set_background_color(c):
    '''
    Set background color in RGB form: (0-255, 0-255, 0-255)
    '''
    global background_color
    background_color = c


def update():
    '''
    Draws the screen for this loop.
    This should always be called at the bottom of game loop
    '''
    window.fill(background_color)
    clock.tick(FPS)

    # check for quit
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()

    sprites.update()

    pygame.display.flip()


def get_mouse_pos():
    return pygame.mouse.get_pos()


def get_mouse_x():
    return pygame.mouse.get_pos()[0]


def get_mouse_y():
    return pygame.mouse.get_pos()[1]


def mouse_clicked():
    state = pygame.mouse.get_pressed()
    return state[0] or state[2]


def get_keys():
    return [e.key for e in pygame.event.get() if e.type is pygame.KEYDOWN] 


def wait(seconds: float):
    global wait_amount
    if wait_amount < seconds:
        wait_amount += 1 / FPS
        return False
    else:
        wait_amount = 0
        return True


def quit():
    pygame.quit()
    exit()

    

