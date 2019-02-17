# coding starts here 

import numpy as np # to run this program make sure you have numpy library. To install numpy (on terminal) : pip install numpy

n_process = int(input('Number of Processes > '))
n_resources = int(input('Number of Resources'))

available_resources = [int(x) for x in input('Claim vector? ').split(' ')]

currently_allocated = np.array(
	[[int(x) for x in input('Currently Allocated for Process ' + str(i + 1) + '? ').split(' ')]for i in range(n_process)])


max_demand = np.array([[int(x) for x in input('MAximum demand for process ' + str(i + 1) + '? ').split(' ')] for i in range(n_process)])


total_available = available_resources - np.sum(currently_allocated, axis=0)

running = np.ones(n_process)  # Basically an array with n_processes 1's to indicate if the process is yet to run


while np.count_nonzero(running) > 0:
	at_least_one_allocated = False
	for p in range(n_process):
		if running[p]:
			if all(i >=0 for i in total_available - (max_demand[p] - currently_allocated[p])):
				at_least_one_allocated = True
				print(str(p) + 'is running')
				running[p] = 0
				total_available += currently_allocated[p]

	if not at_least_one_allocated:
		print('Status: Unsafe')
		exit()

print('Status: Safe')

