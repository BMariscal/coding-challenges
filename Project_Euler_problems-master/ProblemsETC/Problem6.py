"""Find the difference between the sum of the squares of
 the first one hundred natural numbers and the square of the sum."""
 
def sumsqr(i):
	global totalA
	totalA+=(i)**2
	return totalA
	
def sqrsum(i):
    global totalB
    totalB+=i
    return totalB
    
totalA=0
totalB=0
for i in range(1,101):
	sumsqr(i)
	sqrsum(i)
totalB=(totalB)**2
difference=totalB-totalA
	
print('sum of squares: ' + str(totalA))
print('sum of squares: ' + str(totalB))
print('The difference is: ' + str(difference))


