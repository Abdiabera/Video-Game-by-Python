from draw import Drawable
import pygame


class Alien(Drawable):
	def __init__(self, x=0, y=0, size=1, color=(0, 0, 0), visibility=True):
		super().__init__(x, y, visibility)
		self.__size = size
		self.__color = color
		left = x - size
		top = y - size
		self.__rect = pygame.Rect(left, top, size*2, size*2)
		self.__image = pygame.image.load("image.bmp")

	def draw(self, surface):
		if self.get_visible():
			#pygame.draw.circle(surface, self.__color, self.get_position(), self.__size, 0)
			surface.blit(self.__image, self.__rect)

	def get_rect(self):
		pos = self.get_position()
		size = self.get_size()
		left = pos[0] - size
		top = pos[1] - size
		self.__rect = pygame.Rect(left, top, size * 2, size * 2)
		return self.__rect

	def get_size(self):
		return self.__size

	def set_size(self, size):
	    self.__size = size

	def get_color(self):
	    return self.__color

	def set_color(self, color):
	    self.__color = color