class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        word = ""
        for i in range(len(s)):
            if s[i] in word:
                word = word[word.find(s[i]) + 1:]  # set new word starting from the next index of that repeated element
            word += s[i]
            maxlen = max(maxlen, len(word))
        return maxlen
