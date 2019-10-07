import math

eps_max = 1
eps_min = .1 
decay = .00767
step = 0
eps = 0
while(step < 300):

	eps = (eps_max)*math.exp(-decay*step)
	step += 1
	


	print(eps)




