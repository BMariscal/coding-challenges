#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

fraction_positive = 0
fraction_negative = 0
fraction_of_zeroes = 0
for integer in arr:
    if integer > 0:
        fraction_positive += 1
    if integer < 0:
        fraction_negative += 1
    if integer == 0:
        fraction_of_zeroes += 1
print(round(fraction_positive / n,6))
print(round(fraction_negative / n,6))
print(round(fraction_of_zeroes / n,6))
