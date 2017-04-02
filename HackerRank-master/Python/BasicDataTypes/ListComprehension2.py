#Solution with List Comprehension
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

x, y, z, N = (int(input()) for _ in range(4))

print([ [i , j , k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i + j + k != N ])



