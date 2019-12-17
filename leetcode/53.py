class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = 0
        total = None
        for i in nums:
            maxi = max(maxi + i, i)
            if total == None or maxi > total:
                total = maxi
        return total
