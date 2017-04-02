#!/bin/python
#python 2
import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)


primary_diagonal = 0
secondary_diagonal = 0
result = 0
for i in range(n):
    for sublist in a:
        primary_diagonal+=sublist[i]
        i+=1
    break
for j in range(-1,-n,-1):
    for sublnum in a:
        secondary_diagonal+=sublnum[j]
        j-=1
    break

result = abs(primary_diagonal - secondary_diagonal)
print result
