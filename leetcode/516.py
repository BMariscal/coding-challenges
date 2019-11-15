# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
#
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
#
# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len_s = len(s)
        if s == s[::-1]:
            return len_s

        combs = [[0] * len_s for i in range(len_s)]

        for i in range(len_s - 1, -1, -1):
            combs[i][i] = 1
            for j in range(i + 1, len_s):
                if s[i] == s[j]:
                    combs[i][j] = combs[i + 1][j - 1] + 2
                else:
                    combs[i][j] = max(combs[i + 1][j], combs[i][j - 1])

        return combs[0][-1]

