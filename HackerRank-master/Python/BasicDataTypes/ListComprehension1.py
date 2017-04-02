#Solution without List Comprehension
"""
Testcase 0:

Input (stdin)

1
1
1
2

Your Output (stdout)

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Expected Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

"""



x = int(input())
y = int(input())
z = int(input())
N = int(input())
    
"""[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] """

results = []
outer =[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            results.append(i)
            results.append(j)
            results.append(k)
            a=0
            for l in range(0,3):
                a+= results[l]
            if a != N:
                outer.append(results)
                results=[]
            else:
                results=[]
print (outer)