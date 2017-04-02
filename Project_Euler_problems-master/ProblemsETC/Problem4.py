largest=[]
for i in range(100,999+1):
	for j in range(100,999+1):
		dig=str(i*j)
		if dig[0:] == dig[::-1]:
			largest.append(int(dig))
print(max(largest))


