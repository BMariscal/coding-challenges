from time import time

start = time()

total=[]
for i in range(2,101):
	for j in range(2,101):
		total.append(i**j)
#print(total)
count={}
for character in total:
	count.setdefault(character,0)
	count[character]= count[character]+1
print(len(count))

end = time()
print(end - start)


"""ALT SOLUTION using set()
The sets module provides classes for constructing and manipulating unordered 
collections of unique elements. Common uses include membership testing, removing 
duplicates from a sequence, and computing standard math operations on sets such as 
intersection, union, difference, and symmetric difference.

powers = set()

for i in range(2, 101):
        for j in range(2, 101):
                powers.add(i**j)

print(len(powers))
"""


"""
total=[]
for i in range(2,6):
	for j in range(2,6):
		total.append(i**j)
#print(total)
count={}
for character in total:
	count.setdefault(character,0)
	count[character]= count[character]+1
print(len(count))
result={}
for key, value in count.items():
	if key not in result.values():
		result[key] = value
		if value >1:
		    result[key] = value -1
print(len(result))	
print(result)"""

