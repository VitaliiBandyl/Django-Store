def cart_total_amount(request):
	total_bill = 0.0
	try:
		for key,value in request.session['cart'].items():
			total_bill = total_bill + (float(value['price']) * value['quantity'])
	except KeyError:
		pass

	return {'cart_total_amount' : total_bill}
