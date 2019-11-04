# 1st attempt: 7368 ms, O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]
                if total < target:
                    continue
                if total > target:
                    continue
                if total == target:
                    return [i, j]

# 2nd attempt: 56 ms, O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i, val in enumerate(nums):
            if val in dic:
                dic[val].append(i)
            else:
                dic[val] = [i]
        for num in nums:
            second_num = target - num
            in_dict = second_num in dic
            if in_dict and num == second_num and len(dic[num]) > 1:
                return [dic[num][0], dic[second_num][1]]
            elif in_dict and dic[num][0] != dic[second_num][0]:
                return [dic[num][0], dic[second_num][0]]
        return None

