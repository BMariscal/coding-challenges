listOf=[[], []]

def collatz(n):
    collect=[n]
    while n > 1:
        if (n% 2 == 0):
            n = int(n /2)
        elif (n % 2 == 1):
            n=int((3*n)+1)
        collect.append(n)

    global listOf   
    listOf[1] = (collect)
    
    if len(listOf) >1:
        global listOf
        listOf[0] = compare(listOf)
        listOf[1] = []
        
        

def compare(list):
    if (len(list[1])) > (len(list[0])):
        list=list[1]
    else:  
         list=list[0]
    return(list)
    


for inp in range(2,1000000):
    collatz(inp)
    
print(listOf)