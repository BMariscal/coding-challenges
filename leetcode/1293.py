class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])  # dimension

        if k >= m + n - 2: return m + n - 2  # key for speed 668ms -> 52ms

        level = 0
        queue = [(0, 0, 0)]
        visited = set(queue)

        # bfs at most k obstacles
        while queue:
            temp = []
            for i, j, z in queue:
                if i == m - 1 and j == n - 1: return level  # arriving at right corner
                for ii, jj in ((i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)):
                    if 0 <= ii < m and 0 <= jj < n:
                        kk = z + grid[ii][jj]  # update obstacles
                        if kk <= k and (ii, jj, kk) not in visited:  # at most k obstacles
                            temp.append((ii, jj, kk))
                            visited.add((ii, jj, kk))
            level += 1
            queue = temp
        return -1