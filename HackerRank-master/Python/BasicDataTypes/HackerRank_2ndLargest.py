"""""HackerRank: Basic data types > Find the Second Largest Number"""


N=int(input())
string_input = input()
a=list(string_input.split(" "))
T3 = list(map(int,a))
big = max(T3)
while big in T3:
    T3.remove(big)
print(max(T3))

