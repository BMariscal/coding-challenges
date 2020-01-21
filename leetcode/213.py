# dp0, excludes the last house
# dp1, excludes the first house

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        dp0 = [0 for _ in range(len(nums))]
        dp1 = [0 for _ in range(len(nums))]
        dp0[0], dp0[1] = nums[0], max(nums[1], nums[0])
        dp1[1], dp1[2] = nums[1],  max(nums[1], nums[2])
        for i in range(2, len(nums)):
            if i < len(nums) - 1:
                dp0[i] = max(dp0[i - 2] + nums[i], dp0[i - 1])
            if i > 2:
                dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        return max(dp0[-2], dp1[-1])