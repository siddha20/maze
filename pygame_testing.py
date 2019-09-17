import pygame
import sys
import random
pygame.init()



screen=pygame.display.set_mode((900,900))
pygame.display.update()
white=(255,255,255)
black=(0,0,0)

screen.fill(white)
pygame.display.update()
	

while True:
	factor = 1
	for j in range(0,9*factor):
		for i in range(0,9*factor):
			print('hi', j, i)
			rand = random.randint(0,255)
			rand2 = random.randint(0,255)
			rand3 = random.randint(0,255)
			if i%2:
				pygame.draw.rect(screen, (rand2,rand,rand3), (100*i/factor,j*100/factor,100/factor,100/factor), 0)
			else:
				pygame.draw.rect(screen, (rand3,rand2,rand), (100*i/factor,j*100/factor,100/factor,100/factor), 0)
			pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()