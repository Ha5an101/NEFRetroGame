import pygame as pg
from sys import exit

pg.init()

# The original 3:4 aspect ratio calculated using https://calculatorhub.app/aspect-ratio/
width = 600
height = 800
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Pac-Man')
clock = pg.time.Clock()

def QuitGame():
    pg.quit()
    exit()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            QuitGame()

    # Draw elements

    # Update screen
    pg.display.update()
    clock.tick(60)