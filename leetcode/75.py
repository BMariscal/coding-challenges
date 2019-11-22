class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        quicksort: in-place, space complexity= O(1), time complexity=O(nlogn)
        """
        self.quickSort(nums, 0, len(nums) - 1)

    def partition(self, nums, low, high):
        i = (low - 1)
        pivot = nums[high]

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return (i + 1)

    def quickSort(self, nums, low, high):
        if low < high:
            p = self.partition(nums, low, high)

            self.quickSort(nums, low, p - 1)
            self.quickSort(nums, p + 1, high)


