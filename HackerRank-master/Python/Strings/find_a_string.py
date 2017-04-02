"""In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output

2. """

s=input()
snip=input()

total=0
for i in range(0,len(s)):
    if s[i:i+len(snip)] == snip:
        total += 1
print (total)