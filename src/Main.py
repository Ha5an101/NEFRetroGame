import pygame as pg
from sys import exit

pg.init()

# The original 3:4 aspect ratio calculated using https://calculatorhub.app/aspect-ratio/
width = 1080
height = 1440

screen = pg.display.set_mode((width, height))

def QuitGame():
    pg.quit()
    exit()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            QuitGame()

    # Draw elements
    # get from game manager

    # Update screen
    pg.display.update()
