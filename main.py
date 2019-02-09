import ant_colony
import functions
test_nodes = {0: (0, 7), 1: (3, 9)}

def distance(start, end):
	x_distance = abs(start[0] - end[0])
	y_distance = abs(start[1] - end[1])
	import math
	return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))
def findIndex(value, qlist):
	indexValue = -1
	for index, point in qlist.items():
		if point == value:
			indexValue = index
	return indexValue
colony = ant_colony.ant_colony(test_nodes, distance)
answer = colony.mainloop()
print (answer)