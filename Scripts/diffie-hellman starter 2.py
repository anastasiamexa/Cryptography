def is_generator(g, p):
	for i in range(2, p):
		if pow(g, i, p) == g:
			return False
	return True

p = 28151
for g in range(p):
	if is_generator(g, p):
		print(g)
		# the first one found is the smallest, so break
		break