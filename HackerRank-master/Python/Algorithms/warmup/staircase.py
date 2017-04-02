#!/bin/python3

import sys


n = int(input().strip())

total= ''
for i in range(n):
    total += '#'
    print(total.rjust(n))
