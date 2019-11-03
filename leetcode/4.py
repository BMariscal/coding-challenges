# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        working_arr = nums1 + nums2
        arr = self.counting_sort(working_arr)
        fin_arr_len = len(arr)
        median = fin_arr_len // 2
        if fin_arr_len % 2 == 0:
            return (arr[median] + arr[median - 1]) / 2
        return arr[median]

    def counting_sort(self, unsorted):
        final_arr = [0] * len(unsorted)
        low = min(unsorted)
        high = max(unsorted)
        count_array = [0 for i in range(low, high + 1)]
        for i in unsorted:
            count_array[i - low] += 1
        for j in range(1, len(count_array)):
            count_array[j] += count_array[j - 1]
        for k in reversed(unsorted):
            final_arr[count_array[k - low] - 1] = k
            count_array[k - low] -= 1
        return final_arr