#!/bin/python3

import sys


time = input().strip()
if time[-2:]== "PM":
    time= time[:-2]
    if time[0:2] != '12':
        time = str(int(time[0:2])+12) + time[2:]


if time[-2:]== "AM":
    time= time[:-2]
    if time[0:2]== '12':
        time = '00' + time[2:]

print(time)
