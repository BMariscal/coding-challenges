length = int(input('Enter a number between 1 and 26: '))
s = "-"
Alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


Alpha = Alphabet[0:length]
largest = (s.join(Alpha[::-1]+ Alpha[1:]))
maxlen = (len(largest))
#print(largest)
leest = []
for i in range(0,length):
    second_half = (s.join(Alpha[-1:i:-1] + Alpha[i:]))
    leest.append(second_half.center(maxlen, s))
for i in range(len(leest) - 1, 0,-1):
    print(leest[i])
for i in leest:
    print(i)
