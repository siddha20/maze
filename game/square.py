import numpy as np
import pygame
class Square:
	def __init__(self, screen):
		self.size = None
		self.fill = 0
		self.square = None	
		self.position = np.zeros([2])
		self.color = None
		self.screen = screen

	def makeSquare(self, size, position, color):
		self.square = pygame.draw.rect(self.screen, color, (int(position[0]),int(position[1]),size,size), self.fill)
		self.position[0] = position[0]
		self.position[1] = position[1]
		self.color = color
		self.size = size
	def change_color(self, color):
		self.square = pygame.draw.rect(self.screen, color, (int(self.position[0]),int(self.position[1]),self.size,self.size), self.fill)
		self.color = color
	def change_position(self, position):
		self.square = pygame.draw.rect(self.screen, self.color, (int(position[0]),int(position[1]),self.size,self.size), self.fill)
		self.position = position