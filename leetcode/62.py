
"""
Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right


Example 2:

Input: m = 7, n = 3
Output: 28

"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1] * m for i in range(n)]

        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[n - 1][m - 1]


    
