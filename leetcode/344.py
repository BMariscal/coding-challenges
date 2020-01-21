class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        midpoint = len(s) // 2
        left = 0
        right = len(s) - 1

        while left <= midpoint and right >= midpoint:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1



