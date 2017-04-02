#only works for small numbers
n=int(input("What number should I go up to? "))
total=0
for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        total+=p
        print(p)
print ('total is ' + str(total))