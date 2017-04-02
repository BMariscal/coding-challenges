#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

list=a,b,c,d,e
sorted_list = sorted(list)

first = sorted_list[0]+ sorted_list[1] +sorted_list[2]+sorted_list[3]
second = sorted_list[1]+ sorted_list[2] +sorted_list[3]+sorted_list[4]


print(str(first) + ' '+ str(second))
