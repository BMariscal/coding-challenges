def factdigit(x):
	total=1
	for i in range(x,0,-1):
		total*=i
	return total

def factsum(y):
	total=0
	for i in y:
		total+=int(i)
	return total

print(factsum(str(factdigit(100))))
