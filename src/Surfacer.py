import pygame as pg

class MySurface:
	def __init__(self, width: int, height: int, color):
		self.surface = pg.Surface((width, height))
		self.surface.fill(color)

	def DrawSurface(self, screen, pos: set[int]):
		screen.blit(self.surface, pos)

class MyImage(MySurface):
	def __init__ (self, path: str):
		self.surface = pg.image.load(path)

class MyFont(MySurface):
	def __init__ (self, path: str, size: int):
		self.surface = pg.font.Font(path, size)