class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_item = [nums[0]]
        length = len(nums)
        max_dp = first_item + ([0] * (length - 1))
        min_dp = first_item + ([0] * (length - 1))

        for i in range(1, length):
            max_dp[i] = max(max_dp[i - 1] * nums[i], nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(min_dp[i - 1] * nums[i], nums[i], max_dp[i - 1] * nums[i])
        return max(max_dp)