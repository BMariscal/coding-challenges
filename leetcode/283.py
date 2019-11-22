def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    zeroes = 0
    for i in range(length):
        if nums[i] != 0:
            nums[zeroes], nums[i] = nums[i], nums[zeroes]
            zeroes += 1

            # [1, 0, 0, 3, 12]
            # [1, 3, 0, 0, 12]
            # [1, 3, 12, 0, 0]


nums = [0,1,0,3,12]

