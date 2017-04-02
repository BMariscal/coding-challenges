def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

total = 0
i = 1
while fibonacci(i) <= 4000000:
    if fibonacci(i) % 2 == 0:
        total += fibonacci(i)
    i += 1
print(total)