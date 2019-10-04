import tensorflow as tf 
import gym
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import time

def run_action(self, state, sess): # state --> action  need tensorflow sess variable
		return tf.argmax(self.logits, feed_dict={self.states: state.reshape(1, self.action_num)})

	def run_batch(self, states, sess): # states --> action array
		pass
	def train(self, states, future_qval, sess):
		pass