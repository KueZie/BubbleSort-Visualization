import pygame
from random import sample
from json import loads
from pygame.locals import *

pygame.init()

with open("config.json", "r") as f:
    f = f.read()
    f = loads(f)
length = f["length"]
screen_dims = screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode(screen_dims)
scale_x, scale_y = screen_width / length, screen_height / length
clock = pygame.time.Clock()
running = True
paused = False
values = list( range(0, length) )
values = sample(values, len(values))
swapped = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.display.set_caption(f"{f['window_name']} by {f['author']}")

def swap(vals):
    global swapped
    swapped = False
    for i in range( len(vals) - 1 ):
        if vals[i] > vals[i + 1]:
            temp = vals[i]
            vals[i] = vals[i + 1]
            vals[i + 1] = temp
            swapped = True
    return vals

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
    if not paused:
        values = swap(values)
    # Draw
    screen.fill(BLACK)
    for i in range(length):
        pygame.draw.rect(screen, WHITE, Rect(i * scale_x, screen_height - (values[i] * scale_y), scale_x, values[i] * scale_y), 0)

    pygame.display.update()
    clock.tick(120)