from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_occurrences = 0
        item = 0

        for k in c:
            if c[k] > max_occurrences:
                max_occurrences = c[k]
                item = k
        return item
