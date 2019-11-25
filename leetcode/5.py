class Solution:
    # O(n^2)
    def longestPalindrome(self, s: str) -> str:
        pali = s[::-1]
        maxlen = ""
        word = ""
        i = 0
        j = len(s)
        for j in range(len(s), -1,-1):
            i = 0
            while i < j:
                word = s[i:j]
                temp = word[::-1]
                if word  == temp:
                    maxlen = word if len(word) > len(maxlen) else maxlen
                i+=1

        return maxlen


class Solution:
    # O(n)
    def longestPalindrome(self, s: str) -> str:
        if(len(s)==0):
            return ""
        start=0
        maxlen=1
        for i in range(len(s)):
            if(i-maxlen-1>=0 and s[i-maxlen-1:i+1]==s[i-maxlen-1:i+1][::-1]):
                start=i-maxlen-1
                maxlen+=2
            if(i-maxlen>=0 and s[i-maxlen:i+1]==s[i-maxlen:i+1][::-1]):
                start=i-maxlen
                maxlen+=1
        return s[start:start+maxlen]