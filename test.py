def rotate(times, amount, value, limit):
	temp = value
	the_amount = amount
	while times > 0:
		while the_amount > 0:	
			if temp == limit:
				temp = 0
				the_amount -= 1
			else:
				temp += 1
				the_amount -= 1
		times -= 1
		the_amount = amount
	return temp

def unrotate(times, amount, value, limit):
	temp = value
	the_amount = amount
	while times > 0:
		while the_amount > 0:	
			if temp == 0:
				temp = limit
				the_amount -= 1
			else:
				temp -= 1
				the_amount -= 1
		times -= 1
		the_amount = amount
	return temp

print unrotate(1, 2, rotate(1, 2, 5, 5), 5)