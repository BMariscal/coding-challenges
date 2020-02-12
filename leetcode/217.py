class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = set()
        for i in nums:
            n.add(i)

        return not len(nums) == len(n)