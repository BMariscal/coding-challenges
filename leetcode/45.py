class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []
        if len(set(nums)) == 1 and nums[0] == 0:
            return [[0, 0, 0]]

        positivs = [i for i in nums if i > 0]
        if len(positivs) == 0:
            return []

        first_number = set()
        answers = []

        nums.sort()

        if nums[0] > 0 or nums[-1] < 0:
            return []

        for first in range(len(nums) - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            if nums[first] > 0:
                return answers
            low = first + 1
            high = len(nums) - 1
            while low < high:
                target = nums[first] + nums[low] + nums[high]
                if target > 0:
                    high -= 1
                elif target < 0:
                    low += 1
                else:
                    answers.append([nums[first], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
        return answers