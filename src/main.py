import pygame as pg
from sys import exit

pg.init()

width = 800
height = 600

screen = pg.display.set_mode((width, height))

while True:
    # Close the Window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Draw elements


    # Update screen
    pg.display.update()