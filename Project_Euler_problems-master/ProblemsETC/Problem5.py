check_list = [11, 13, 14, 16, 17, 18, 19, 20]
count = {}
for i in range(2520,999999999, 2520):
	it_works = True
	for j in check_list:
		if i % j != 0:
			it_works = False
			break
	if (it_works):
		print(i)
		break
	# for i in range(0,21):
	# 	print(i)

#print(count)
#maximum = (max(count, key=count.get))
#print (maximum)
#print (count[maximum])




