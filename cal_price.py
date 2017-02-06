def cal_price(BEY,CPR,cpn,ori_term):
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
		interest = act_bal[i]*cpn/1200.0
		total = float(act_prin+interest)
		PV_BEY[i] = total/((1.0+BEY/200.0000000000000)**(age[i]/6.00))
		PV_yrs[i] = age[i]/12.0*PV_BEY[i]
	mod_dur = (sum(PV_yrs)/sum(PV_BEY))/(1+BEY/200.0)
	print "Price:",sum(PV_BEY)

cal_price(7.40184,5,7,30)
cal_price(8.006,10,7,30)
cal_price(7.006,10,7,30)
cal_price(8.006,5,7,30)
cal_price(7.006,15,7,30)