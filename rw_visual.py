import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk()
	rw.fill_walk()
	plt.scatter(rw.x_values,rw.y_values,s=15)
	plt.show()
	run = input("continue?")
	if run == 'n':
		break
