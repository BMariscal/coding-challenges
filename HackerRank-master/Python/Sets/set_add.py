# If we want to add a single element to an existing set, we can use the .add() operation.
# It adds the element to the set and returns 'None'.
#
# Example
#
# >>> s = set('HackerRank')
# >>> s.add('H')
# >>> print s
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# >>> print s.add('HackerRank')
# None
# >>> print s
# set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])


#solution 1
def countries(x):
    print(len(set(x)))







if __name__ == '__main__':
    size= int(input())
    list=[]
    for i in range(size):
        list.append(input())
    countries(list)

#solution 2

print(len(set([input()for i in range(int(input()))])))
