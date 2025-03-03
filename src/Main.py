import pygame as pg
from sys import exit
import GameManager

pg.init()

# The original 3:4 aspect ratio calculated using https://calculatorhub.app/aspect-ratio/
width = 600
height = 800
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Pac-Man')

famerate = 60
clock = pg.time.Clock()

game = GameManager.Game()
continueGameLoop = game.StartGame()

def QuitApp():
    pg.quit()
    exit()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            QuitApp()
    
    keys = pg.key.get_pressed()
    
    if continueGameLoop:
        continueGameLoop = game.UpdateGame()
    else:
        if keys[pg.K_SPACE]:
            continueGameLoop = game.RestartGame()
        if keys[pg.K_ESCAPE]:
            continueGameLoop = game.EndGame()
            QuitApp()

    # Update screen
    pg.display.update()
    clock.tick(famerate)