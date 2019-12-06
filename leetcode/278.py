# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left_most = 0
        right_most = n
        while left_most <= right_most:
            midpoint = ((right_most - left_most) // 2) + left_most
            if not isBadVersion(midpoint):
                left_most = midpoint + 1
            else:
                right_most = midpoint - 1

        return left_most
