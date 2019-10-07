import numpy as np
import random 
import math 

class Q:
	def __init__(self, max_frame):
		self.num_states = None
		self.num_actions = None
		self.Q_table = None

		self.eps_max = None
		self.eps_min = None
		self.eps_val = None
		self.decay = None

		self.max_frame = max_frame

	def create(self, num_states, num_actions):
		self.num_states = num_states
		self.num_actions = num_actions
		self.Q_table = np.zeros([self.num_states, self.num_actions])

	def set_decay_variables(self, eps_max, eps_min, decay):
		self.eps_max = eps_max
		self.eps_min = eps_min
		self.eps_val = self.eps_max
		self.decay = (math.log((self.eps_min)/(self.eps_max)))/(-self.max_frame)
	def choose_actions(self):
		pass
	def decay(self, step):
		eps = (self.eps_max)*math.exp(-self.decay*step)
		return eps 




