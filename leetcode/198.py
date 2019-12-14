class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)

        previous = nums[0]
        maxi = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = maxi
            curr = nums[i]
            maxi = max(curr + previous, maxi)
            previous = temp
        return maxi