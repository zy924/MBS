from sympy import *
from scipy.optimize import fsolve
def cal_bey(price,CPR,cpn,ori_term):
	SMM = 100.00*(1-pow(1-CPR/100.0,1/12.0))
	age = [i+1.0 for i in xrange(ori_term*12)]
	nage = len(age)
	sched_bal = [0 for x in xrange(nage+1)]
	act_bal = [0 for x in xrange(nage+1)]
	sched_bal[0]=100.0
	act_bal[0]=100.0
	for i in xrange(1,nage+1):
		sched_bal[i] = (1-(pow(1+cpn/1200.0,age[i-1])-1)/(pow(1+cpn/1200.0,ori_term*12.0)-1))*100.0
		act_bal[i] = sched_bal[i]*pow(1-SMM/100.0,age[i-1])
	#act_prin = [0 for x in xrange(nage)]
	#interest = [0 for x in xrange(nage)]
	#total = [0 for x in xrange(nage)]
	def func(i):			
		BEY = i[0]
		PV_BEY = [0 for x in xrange(nage)]
		for i in xrange(nage):
			act_prin = act_bal[i]-act_bal[i+1]
			interest = act_bal[i]*cpn/1200
			total = act_prin+interest
			PV_BEY[i]  = total/(pow(1+BEY/200.0,age[i]/6.0))
		return [price-sum(PV_BEY)]
	r = fsolve(func,[7.0])
	print "price:",price
	print "CPR:",CPR
	print "BEY:",round(r,3)
	return round(r,3)

def cal_mdur(BEY,CPR,cpn,ori_term):
	SMM = 100.00*(1-pow(1-CPR/100.0,1/12.0))
	age = [i+1.0 for i in xrange(ori_term*12)]
	nage = len(age)
	sched_bal = [0 for x in xrange(nage+1)]
	act_bal = [0 for x in xrange(nage+1)]
	sched_bal[0]=100.0
	act_bal[0]=100.0
	PV_BEY = [0 for x in xrange(nage)]
	PV_yrs = [0 for x in xrange(nage)]
	for i in xrange(1,nage+1):
		sched_bal[i] = (1-(pow(1+cpn/1200.0,age[i-1])-1)/(pow(1+cpn/1200.0,ori_term*12.0)-1))*100.0
		act_bal[i] = sched_bal[i]*pow(1-SMM/100.0,age[i-1])
	for i in xrange(nage):
		act_prin = act_bal[i]-act_bal[i+1]
		interest = act_bal[i]*cpn/1200
		total = act_prin+interest
		PV_BEY[i] = total/(pow(1+BEY/200.0,age[i]/6.0))
		PV_yrs[i] = age[i]/12.0*PV_BEY[i]
	mod_dur = (sum(PV_yrs)/sum(PV_BEY))/(1+BEY/200.0)
	print "mod_dur:",round(mod_dur,3)
	print "Price:",sum(PV_BEY)

CPR = [5,10,15]
Price = [98,100,102]
for p in xrange(3):
	for j in xrange(3):
		BEY = cal_bey(Price[p],CPR[j],7,30)
		cal_mdur(BEY,CPR[j],7,30)

