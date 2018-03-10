def boxPrint(symbol, width, height):
	if len(symbol) > 1:
		raise Exception('Symbol length must be 1.')

	print(symbol * width)

	for i in range(height - 2):
		print(symbol + (' ' * (width - 2) + symbol))

	print(symbol * width)	

boxPrint('**', 8, 8)