import math
import random

for i in range(0,100):

	x = random.uniform(-10000,10000)
	y = random.uniform(-10000,10000)
	print("Run Number: %s" %(i))

	print("Initial Random x,y: %s,%s"%(x,y))
	fun = (-(y+47)*math.sin(math.sqrt(abs((x/2)+(y+47))))-x*math.sin(math.sqrt(abs(x-(y+47)))))
	for i in range(0,99):
		xnew = (random.uniform(0,1) - 0.5)*0.1 + x
		ynew = (random.uniform(0,1) - 0.5)*0.1 + y
		print("Step Number: %s" %(i))
		print ("New x and y values for each Run: %s,%s"%(xnew,ynew))
		while True:
			if(xnew < 10000 and ynew < 10000):
				break
			else:
				# print "hi"
				xnew = (random.uniform(0,1) - 0.5)*0.1 + x
				ynew = (random.uniform(0,1) - 0.5)*1.0 + y
		newfun = (-(ynew+47)*math.sin(math.sqrt(abs((xnew/2)+(ynew+47))))-xnew*math.sin(math.sqrt(abs(xnew-(ynew+47)))))
		print ("old Function value is %s,optimized function value is %s"%(fun,newfun))
		if (newfun < fun):
			#print x,y
			#print xnew, ynew
			#print fun
##			x = xnew
##          y = ynew
##          fun = newfun
			print("Optimized Function Value: %s"%(newfun))
			# print i
			break
		
		x = xnew
		y = ynew
		fun = newfun
		
