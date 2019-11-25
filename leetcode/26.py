class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return length
        i = 0
        while i != len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i+=1
        return len(nums)

