"""
The rule to calculate the shortest distance move between 2 sets of points is just the maximum of the difference between corresponding coordinates of 2 input sets of points:
In other words, you need to move at least the longest distance between corresponding coordinates in order to get to the point
for example:
[-111, 222] and [0, 15]
abs(-111-0) = 111
abs(222 - 15) = 207
Then we need to move 207 to get to [0, 15]

Then we read 2 sets of points at a time and sums the distance up

"""



class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def rule(A, B):
            return max(abs(A[0] - B[0]), abs(A[1] - B[1]))

        sum = 0

        for tup1, tup2 in zip(points[:-1], points[1:]):
            sum += rule(tup1, tup2)

        return sum