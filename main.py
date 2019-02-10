import PSO
import functions

number = input("What function do you want to test? \n press 1 for ackley \n press 2 for sumOfSquare \n press 3 for sphere\n")
func = functions.functions()
initial=[5,5]               # initial starting location [x1,x2...]
bounds=[(-5,5),(-5,5)] # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
try:
	val = int(number)
	if val == 1:
		PSO.PSO(func.ackley, initial, bounds, num_particles=15, maxiter=30, verbose=True)
	elif val == 2:
		PSO.PSO(func.sumOfSquare, initial, bounds, numa_particles=15, maxiter=30, verbose=True)
	elif val == 3:
		PSO.PSO(func.sphere, initial, bounds, num_particles=15, maxiter=30, verbose=True)
	else:
		print("Invalid Input")
except ValueError:
   print("That's not an int!")
   print("No.. input string is not an Integer. It's a string")


