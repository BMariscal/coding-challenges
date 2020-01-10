# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.



class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        record = {}
        oldest, res = 0, 0
        for i, c in enumerate(s):
            record[c] = i
            if len(record) > k:
                oldest = min(record.values())
                del record[s[oldest]]
                oldest += 1
            res = max(i - oldest + 1, res)
        return res



