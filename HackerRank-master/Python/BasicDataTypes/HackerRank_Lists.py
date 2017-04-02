
"""HackerRank: Basic data types > Lists"""

if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(n):
        message = [str(chunk) for chunk in input().strip().split(' ')]
        #print(message)
       

        
        
        if (message[0] == "insert"):
            list.insert(int(message[1]),int(message[2]))
        if (message[0] == "print"):
            print (list)
        if (message[0] == "remove"):
            list.remove(int(message[1]))
        if (message[0]== "append"):
            list.append(int(message[1]))
        if (message[0] == "sort"):
            list.sort()
        if (message[0] == "pop"):
            list.pop()
        if (message[0] == "reverse"):
            list.reverse()
            
    
