"""One of the reasons the script is slow is that you're building an array.
Over time, the array will become quite large and the performance degrades.
 Since the answer I'm looking for is a singular value, why not optimize
  out the need to have an array
"""
n=13
x=6
count=[]
for i in range(2,n+1):
	for j in range(2,i):
		if i % j == 0:
			break
	else:
		count.append(i)

print (count[x-1])
