import numpy as np
import random 
import math 

''' Q(s, a) = Q(s, a) + learning rate[reward + discount(maxQ'(s', a')) - Q(s, a)] '''

class Q:
	def __init__(self, max_frame):
		self.num_states = None
		self.num_actions = None
		self.table = None

		self.eps_max = None
		self.eps_min = None
		self.eps_val = None
		self.decay = None

		self.discount_rate = None
		self.learning_rate = None

		self.max_frame = max_frame

		self.test = None

	def create_table(self, size, num_actions):
		self.num_states = size * size
		self.num_actions = num_actions
		self.table = np.ones([self.num_states, self.num_actions])

	def set_variables(self, learning_rate, discount_rate):
		self.learning_rate = learning_rate
		self.discount_rate = discount_rate

	def set_decay_variables(self, eps_max, eps_min):
		self.eps_max = eps_max
		self.eps_min = eps_min
		self.eps_val = self.eps_max
		self.decay = (math.log((self.eps_min)/(self.eps_max)))/(-self.max_frame)

	def up_decay(self, amount):
		self.decay += amount

	def eps_decay(self, frame):
		self.eps_val = self.eps_max*math.exp(-self.decay * frame)
		return self.eps_val

	def update_table(self, prev_state, state, action, reward):
		Q_sa = self.table[int(prev_state)][int(action)]
		self.table[int(prev_state)][int(action)] = Q_sa + (self.learning_rate*(reward + (self.discount_rate*np.argmax(self.table[int(state)])) - Q_sa))
		
	def get_action(self, state):
		self.test = 2
		if ((random.randint(0,10000)/10000) < self.eps_val):
			self.debug = 'RANDOM'
			return random.randint(0, self.num_actions-1)
		else:
			self.debug = 'STATE'
			return np.argmax(self.table[state])
		


