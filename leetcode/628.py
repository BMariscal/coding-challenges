class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sort = sorted(nums)
        one = sort[0] * sort[1] * sort[-1]
        two = sort[0] * sort[-2]  * sort[-1]
        three = sort[-3] * sort[-2] * sort[-1]
        four = sort[0] * sort[1] * sort[2]
        return max(one, two, three, four)
