def lit_compare(a,b):
	if a == b:
		print(1)
	elif len(a) > len(b):
		print(2)
	elif b == 'learn':
		print(3)
	
	
lit_compare("I am not a monster","learn")