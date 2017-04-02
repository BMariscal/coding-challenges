#to execute, needs to be executed with Numbers2.txt, that's where the data is
#Briceidas-MacBook-Pro:Desktop briceida$ python3 Problem13.py Numbers2.txt
#(change Desktop to ProjectEuler)
import sys

#iterates over list in chunks
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

#Reads filename from directory. Data was saved into text file. s is content in file 
s = ''

def readIn(filename):
	with open(filename) as f:
		global s
		s = f.readlines()

#Numbers2.txt is argv[1]
readIn(sys.argv[1])

total=0 
def tally():
	print(s)
	for group in chunker(s[0], 50):
		print('Group: ' + group)

		global total
		total+=int(group)
		print('Total: ' + str(total))

tally()
