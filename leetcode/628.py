class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sort = sorted(nums)
        one = sort[0] * sort[1] * sort[-1]
        three = sort[-3] * sort[-2] * sort[-1]
        return max(one, three)
