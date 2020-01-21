"""
Keep a variable: level, to represent a new unique value we will give to each position in sorted array A.

During iteration:

1. If level < current element of sorted(A), it means we find a new unique value for this position,
 just make level equal to this element and don't need make increment;

2. If level >= current element of sorted(A), it must be one scenario that sorted(A)[i] == sorted(A)[i-1],
just make one simple increment of level to make it unique for current postion and add the difference between
 incremented level and current value to result.




"""

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        level = -1
        res = 0

        for x in sorted(A):
            if level < x:
                level = x
            else:
                level += 1
                res += level - x

        return res