import pygame
import sys
import random
import math
import numpy as np
np.random.seed(238)
random.seed(238)
pygame.init()

screen=pygame.display.set_mode((1000,1000))
pygame.display.update()

screen.fill((0,0,0))
pygame.display.update()

square = pygame.draw.rect(screen,(255,255,255), 
			(320,240,100,100),5)

class Player: 
	def __init__(self):
		self.location = None
		self.actions = [0,1,2,3] #up down left right
	def move(self):
		pass
class Grid: 
	def __init__(self, num_traps):
		self.screen_x, self.screen_y = screen.get_size()
		self.num_squares = 100
		self.positions = np.zeros([10,10])
		self.num_traps = num_traps
	def model_screen(self): 
		trap_positions = np.random.choice(100, self.num_traps)
		goal_positions = 
		count = 0
		for position in self.positions:
			for square in position:

				square =
				count += 1
class Square: 
	def __init__(self, size):
		self.Q_value = None
		self.reward = None
		self.type = None
		self.size = size
	def make_normal(self, x, y):
		self.type = 0
		self.reward = 10
		pygame.draw.rect(screen,(0,0,0), 
			(x,y,self.size,self.size),0)
	def make_trap(self, x, y):
		self.type = 1
		self.reward = -100
		pygame.draw.rect(screen,(255,0,0), 
			(x,y,self.size,self.size),0)
	def make_goal(self, x, y):
		self.type = 2
		self.reward = 100
		pygame.draw.rect(screen,(0,255,0), 
			(x,y,self.size,self.size),0)
class GameRunner: 
 	def __init__(self):
 		pass
test = Grid(3)
test.model_screen()


while True:

	pygame.display.update()
	for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()