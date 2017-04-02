import string
def number_needed(a, b):
    s = string.ascii_lowercase
    count = 0
    for char in s:
        count += abs(a.count(char)-b.count(char))
    return count



a = input().strip()
b = input().strip()

print(number_needed(list(a), list(b)))
