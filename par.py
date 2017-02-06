import numpy as np
from sympy import *

# calculate spot yield from par yield
def solve_spot(i,year,par,spot):
	x = symbols('x')
	temp1 = 0.0
	for k in xrange(i):
		temp1 += (par[i]/2.0)/(pow(1+spot[k]/200.0,k+1))
	temp2 = (100+par[i]/2)/(pow(1+x/200,i+1))
	result = solve(100- temp1-temp2,x)
	m = len(result)
	for ind in xrange(m):
		if result[ind]>0:
			return round(result[ind],3)

#calculate forward from par
def solve_forward(i,year,forward,spot):
	x = symbols('x')
	temp1 = 1.0
	for k in xrange(i):
		temp1 = temp1*(1+forward[k]/200)
	temp1 = temp1*(1+x/200)
	temp2 = pow((1+spot[i]/200),(i+1))
	result = solve(temp1-temp2,x)
	m = len(result)
	for ind in xrange(m):
		if result[ind]>0:
			return round(result[ind],3)

def cal(year, par):
	n = len(par)
	spot = [0 for x in xrange(n)]
	spot[0] = par[0]
	for i in xrange(1,n):
		spot[i] = float(solve_spot(i,year,par,spot[:i]))
	print "spot",spot
	forward = [0 for x in xrange(n)]
	forward[0] = spot[0]
	for i in xrange(1,n):
		forward[i] = float(solve_forward(i,year,forward[:i],spot))
	print "forward",forward
	
#default input data
year = [.5,1.0,1.5,2.0]
par = [3.5,3.5,3.5,3.5]

cal(year,par)
for i in xrange(3):
	print 1.75/((1+3.5/200)**(i+1))
print 101.75/((1+3.5/200)**4)
