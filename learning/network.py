import tensorflow as tf 
import gym
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import time

class Network: # class to train the maze
	def __init__(self, memory_size, decay, discount_rate, states, actions, state_num, action_num, layer_num):

		self.memory_size = memory_size # array size to hold current and future states
		self.decay = decay # decay number eps decay
		self.discount_rate = discount_rate # used to tune future reward worth

		self.states = states 
		self.actions = actions
		self.state_num = state_num
		self.action_num = action_num
		self.layer_num = layer_num

		# placeholders
		self.states = None
		self.future_qval = None

		# tensor vars
		self.logits = None
		self.optimize = None
		self.var_init = None
		#setup the network
		self.network() # the classes network 

	def network(self):
		self.states = tf.placeholder(tf.float32, [None,self.state_num]) # input for the NN
		self.future_qval = tf.placeholder(tf.float32, [None, self.action_num]) # input for the future q val that was run after 
		# desnse network design 
		layer1 = tf.layers.dense(self.states, self.layer_num, activation=tf.nn.relu)
		layer2 = tf.layers.dense(layer1, self.layer_num, activation=tf.nn.relu)
		# logits don't have a activation done to it... it is the raw value.
		self.logits = tf.layers.dense(layer2, self.action_num)
		error = tf.losses.mean_squared_error(future_qval, states)
		self.optimize = tf.train.AdamOptimzer().minimize(error)
		self.var_init = tf.global_variables_initializer()

	






