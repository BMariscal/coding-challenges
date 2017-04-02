#learned the use of capitalize(), replace() and split()

"""You are given a string S. Your task is to capitalize each word of S ."""
S = input()
T = S[:].split()
for i in T:
    S = S.replace(i, i.capitalize())
print(S)