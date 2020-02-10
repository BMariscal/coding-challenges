class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_window_max = 0
        right_window_max = 0
        max_amount = float("-inf")

        while left < right:
            left_window_max = max(height[left], left_window_max)
            right_window_max = max(height[right], right_window_max)
            diff = min(right_window_max, left_window_max)
            max_amount = max(max_amount, diff * (right - left))

            if left_window_max > right_window_max:
                right -= 1

            elif right_window_max > left_window_max:
                left += 1

            else:

                left += 1
                right -= 1

        return max_amount

