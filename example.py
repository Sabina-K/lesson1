def get_vat(payment, percent=18):
	try: 
		payment = float(payment)
		percent = int(percent)
		vat = payment / 100 * percent
		vat = round(vat, 2)
		return "сумма ндс: {}".format(vat)
	except (TypeError, ValueError):
		return "не могу посчитать"
    	

result = get_vat(10)	
print(result)