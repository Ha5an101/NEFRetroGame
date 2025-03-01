import pygame as pg
from IObject import GameObject

class SurfaceObject(GameObject):
	def __init__(self, pos: list[int], dirc: list[int], width: int, height: int, color):
		super().__init__(pos, dirc)

		self.surface = pg.Surface((width, height))
		self.copy_surface = self.surface.copy()
		self.surface.fill(color)

	def DrawSurface(self, screen):
		screen.blit(self.copy_surface, self.pos)

	def AlignSurface(self):
		self.copy_surface = pg.transform(self.surface, True if self.direction[1] <= 0 else False, True if self.direction[0] <= 0 else False)

class ImageObject(SurfaceObject):
	def __init__ (self, pos: list[int], dirc: list[int], path: str):
		GameObject.__init__(pos, dirc)
		self.surface = pg.image.load(path).convert_alpha()

class TextObject(SurfaceObject):
	def __init__ (self, pos: list[int], dirc: list[int], path: str, size: int):
		GameObject.__init__(pos, dirc)
		self.surface = pg.font.Font(path, size)

class SpriteObject(SurfaceObject, pg.sprite.Sprite):
	def __init__ (self, pos: list[int], dirc: list[int], width: int, height: int, color):
		SurfaceObject.__init__(pos, dirc, width, height, color)
		pg.sprite.Sprite.__init__(self)