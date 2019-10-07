from game.grid import Grid
from game.player import Player
from game.game import Game
from game.rendered_grid import RenderedGrid

from learning.q import Q

from train import Train

import pygame
import numpy as np
import random
import time



if __name__ == "__main__":
	train = Train()

	train.make_game(traps=0, size=9, square_size=40, frame_limit=100, rendered=True)
	train.run_game(epochs=10)



	



	

	


