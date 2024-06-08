import abc

class Drawable(metaclass=abc.ABCMeta):
	def __init__(self, x=0, y=0, visibility=True):
	  	self.__x = x
	  	self.__y = y
	  	self.__visible = visibility

	def get_position(self):
		return self.__x, self.__y

	def set_position(self, position):
		self.__x = position[0]
		self.__y = position[1]

	def set_visible(self, visibility):
		self.__visible = visibility

	def get_visible(self):
		return self.__visible

	@abc.abstractmethod
	def get_rect(self):
		pass

	@abc.abstractmethod
	def draw(self, surface):
		pass