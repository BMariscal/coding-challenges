import heapq
import math


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = math.inf
        q = [x for x in points]
        heapq.heapify(q)

        max_y_line = {}

        while len(q) > 0:
            top = q[0][0]
            ps = []

            # get all the (x,y) pairs for this x
            while len(q) > 0 and q[0][0] == top:
                ps.append(heapq.heappop(q))

            lines = []

            if len(ps) > 1:
                x = ps[0][0]

                # generate all the combinations of left side lines
                for i in range(len(ps) - 1):
                    for j in range(i + 1, len(ps)):
                        lines.append((ps[i][1], ps[j][1]))

                # for all the combos, if a line has occurred before calculate the area
                for line in lines:
                    if line in max_y_line:
                        xmin = max_y_line[line]
                        min_area = min(min_area, self.area(xmin, x, line[0], line[1]))
                    max_y_line[line] = x

        return min_area if min_area != math.inf else 0

    def area(self, x1, x2, y1, y2):
        return abs(x2 - x1) * abs(y2 - y1)