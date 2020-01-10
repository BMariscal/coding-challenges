# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1)
# are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.
#
# Two rectangles overlap if the area of their intersection is positive.
# To be clear, two rectangles that only touch at the corner or edges do not overlap.
#
# Given two (axis-aligned) rectangles, return whether they overlap.
#
# Example 1:
#
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# Example 2:
#
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# Notes:
#
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # [x1, y1, x2, y2]

        [x1rec1,y1rec1,x2rec1,y2rec1], [x1rec2,y1rec2,x2rec2,y2rec2] = rec1, rec2
        return y1rec2<y2rec1 and x1rec2<x2rec1 and y1rec1<y2rec2 and x1rec1<x2rec2



rec1 = [0,0,2,2]
rec2 = [1,1,3,3]