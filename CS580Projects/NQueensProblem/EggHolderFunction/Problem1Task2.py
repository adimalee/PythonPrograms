import random
import math
import copy

# Global Declarations
numpop = 100
F = 0.1
Waste = []
list = {}
newlist = {}


def funcval(x,y):                                                               # Function Declaration for Egg Holder Function
	fun = (-(y+47)*math.sin(math.sqrt(abs((x/2)+(y+47))))-x*math.sin(math.sqrt(abs(x-(y+47)))))
	return fun

for i in range(0,100):                                                          # 100 Runs
	minimumlist = []
	for j in range (0,100):                                                 # Generate 100 x and y values and store it into a list
		x = random.uniform(-10000,10000)
		y = random.uniform(-10000,10000)
		newlist[j] = (x,y)
	# print newlist
	
	for k in range(0,100):                                                  # 100 Steps
		list = newlist.copy()
		for i in range(0,numpop):
			a = random.sample(range(0,numpop),3)
			while True:
				if i not in a:
					Waste = a
					# print Waste
					break
				else:
					a = random.sample(range(0,numpop),3)
			# print Waste
			# print list[Waste[0]]
			val1 = list[Waste[0]][0]+(F*(list[Waste[1]][0]-list[Waste[2]][0]))
			val2 = list[Waste[0]][1]+(F*(list[Waste[1]][1]-list[Waste[2]][1]))
			# print (val1,val2)
			
			rndnum = random.uniform(0,1)                            # Generate random number between 0 and 1
				# print u
			if(rndnum < 0.1):
				X1 = val1
			else:
				X1 = list[i][0]
			rndnum = random.uniform(0,1)
				# print u
			if(rndnum < 0.1):
				X2 = val2
			else:
				X2 = list[i][1]
			# print (U1,U2)
			newval = funcval(X1,X2)                                 # Calculating the new function value with updated x and y points
			oldval = funcval(list[i][0],list[i][1])                 # Calculating the old function value with previous x and y points
			# print newval,oldval
			if (newval < oldval):                                   # Checking to see if the new function value is lower to find global minimum
				newlist[i] = (X1,X2)
			else:
				newlist[i] = (list[i][0],list[i][1])
				
	# print newlist
	for i in range(0,100):                                                  # Print 100 runs of the local minimum values until we reach the global minimum
		minimumlist.append(funcval(newlist[i][0],newlist[i][1]))
	# print minimumlist
	globalminimumlist = min(minimumlist)
	#print globalminimumlist
	
if(globalminimumlist < minimumlist):                                            # Prints the global minimum if found in the minimumlist
    print ("GlobalMinimum: %s" %(globalminimumlist))
else:
    print ("LocalMinimum: %s" %(minimumlist))

