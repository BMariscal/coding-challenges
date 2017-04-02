f = open("names.txt", "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                             # Note: if you want to write to the file use "w" as second argument
lis=[]
a= (f.read())

b=(a.split(','))

for i in b:
	i=i.replace('"', '')
	lis.append(i)
lis.sort();

f.close()                   # It's important to close the file to free up any system resources.


letters={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,
 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
final=0
for i in lis:
	holder=0
	for j in i:
		if j in letters:
			holder+=(letters[j])
	x=(holder)
	y=(lis.index(i))+1
	z=(x*y)
	final+=z
print(final)

