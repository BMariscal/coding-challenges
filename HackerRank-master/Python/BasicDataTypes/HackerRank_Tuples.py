"""""HackerRank: Basic data types > Lists"""

if __name__ == '__main__':
    n = int(input())
    
    
    test = input().split()
    #print(test)
    """map turns strings inside list into integers: http://stackoverflow.com/questions/10145347/convert-string-to-integer-using-map"""
    integer_list = list(map(int, test))
    #print(integer_list)
    a=tuple(integer_list)
    print(hash(a))
   