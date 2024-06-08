from draw import Drawable
import pygame

class Block(Drawable):
	def __init__(self, x=0, y=0, size=1, color=(0, 0, 0), visibility=True):
		super().__init__(x, y, visibility)
		self.__size = size
		self.__color = color
		self.__rect = pygame.Rect(x, y, size, size)
	def draw(self, surface):
		if self.get_visible():
			outline_color = (0, 0, 0)
			outline_width = 2
			#Draw a filled rectanygame.draw.rect(surface, self.__color, self.__rect, 0)
			#Draw the outline around the rectangle
			pygame.draw.rect(surface, outline_color, self.__rect, outline_width)

	def get_rect(self):
		pos = self.get_position()
		size = self.get_size()
		self.__rect = pygame.Rect(pos[0], pos[1], size, size)
		return self.__rect

	def get_size(self):
		return self.__size

	def set_size(self, size):
		self.__size = size

	def get_color(self):
		return self.__color

	def set_color(self, color):
		self.__color = color