
# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

# >>> print 'ab123'.isalnum()
# True
# >>> print 'ab123#'.isalnum()
# False

# str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).

# >>> print 'abcD'.isalpha()
# True
# >>> print 'abcd1'.isalpha()
# False

# str.isdigit()
# This method checks if all the characters of a string are digits (0-9).

# >>> print '1234'.isdigit()
# True
# >>> print '123edsd'.isdigit()
# False

# str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).

# >>> print 'abcd123#'.islower()
# True
# >>> print 'Abcd123#'.islower()
# False

# str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).

# >>> print 'ABCD123#'.isupper()
# True
# >>> print 'Abcd123#'.isupper()
# False



def tests(j,y):

    if j == 1:
        z=y.isalnum()
        return z
    elif j == 2:
        z=y.isalpha()
        return z
    elif j == 3:
        z=y.isdigit()
        return z
    elif j == 4:
        z=y.islower()
        return z
    elif j == 5:
        z=y.isupper()
        return z       


a=input()
a=str(a)

for j in range(1,6):
    list=[]
    for i in range(0,len(a)):
        y=a[i]
        list.append(tests(j,y)) 
    print_true = False
    for i in list:
            
        if i == True:
            print_true = True
            
    print(print_true)
    
          


"""better solution:
str = raw_input()
print any(c.isalnum()  for c in str)
print any(c.isalpha() for c in str)
print any(c.isdigit() for c in str)
print any(c.islower() for c in str)
print any(c.isupper() for c in str)
"""