class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[target] == True:
                    return True
                if dp[i]:
                    dp[i] = dp[i]
                elif dp[i - num]:
                    dp[i] = dp[i - num]
        return dp[target]