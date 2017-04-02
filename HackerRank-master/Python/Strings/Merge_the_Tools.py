#Hackerrank, Merge the Tools!
#python > strings > Merge the Tools!
"""Sample Input

AABCAAADA
3   

Sample Output

AB
CA
AD
"""

def merge_the_tools(string, k):
    for i in range(0,len(string)+1, k):
        pre_work=(string[i:i+k])
        print(''.join(sorted(set(pre_work), key=pre_work.index)))