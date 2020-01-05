# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.

# O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        n1, n2 = 1, 1

        for i in range(2, n + 1):
            n1, n2 = n2, n1 + n2

        return n2


    # input: 35, output: 14930352


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]