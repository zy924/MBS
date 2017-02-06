def bey_change(price,dur,bp):
	price_plus = price + price*(-dur)*bp/10000
	price_minus = price - price*(-dur)*bp/10000
	return [price_plus,price_minus]

print bey_change(98,3.866,50)