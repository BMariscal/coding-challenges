# solved with forloop, modulo operator, list append() method and conditional statements 
#Return the string representation of numbers from 1 to n

    #Multiples of 3 -> 'Fizz'
    #Multiples of 5 -> 'Buzz'
    #Multiples of 3 and 5 -> 'FizzBuzz'

expected = [
    '1',
    '2',
    'Fizz',
    '4',
    'Buzz',
    'Fizz',
    '7',
    '8',
    'Fizz',
    'Buzz',
    '11',
    'Fizz',
    '13',
    '14',
    'FizzBuzz'
]



def fizz_buzz(num):
    arr =[]
    for i in range(1,num+1):
        if i%3 == 0 and i% 5 == 0:
            arr.append('FizzBuzz')
        elif i % 3 ==0:
            arr.append('Fizz')
        elif i % 5 == 0:
            arr.append('Buzz')
        else:
            arr.append(str(i))
    return arr
    
print(fizz_buzz(15) == expected) #True
