def safe_div(x,y):
	if y != 0:
		z = int(x / y)
		print(z)
		return z
	else:
		print("На ноль делить нельзя!")

safe_div(4,0)