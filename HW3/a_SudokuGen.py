letters = ['nothing', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
for x in range(1, 10):
	for y in range(1, 10):
		#unary constraints
		print letters[x] + str(y), 'gt', 0
		print letters[x] + str(y), 'lt', 10
		#row constraints
		for x2 in range(1, 10):
			if x != x2:
				print letters[x] + str(y), 'ne', letters[x2] + str(y)
		#column constraints
		for y2 in range(1, 10):
			if y != y2:
				print letters[x] + str(y), 'ne', letters[x] + str(y2)
		#block constraints
		for 