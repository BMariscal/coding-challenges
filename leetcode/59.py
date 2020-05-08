class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return

        matrix = [([1] * n) for i in range(n)]
        nums = [i for i in range(1, (n * n) + 1)]

        def isvalid(row, column):
            return (0 <= row <= len(matrix) - 1) and (0 <= column <= len(matrix[0]) - 1)

        def visit(row, column, visited, nums):
            if (row, column) in visited:
                return
            if len(nums) == 0:
                return

            if not isvalid(row, column):
                return
            nonlocal last_visited

            visited.add((row, column))
            matrix[row][column] = nums[0]
            up = (row - 1, column)
            down = (row + 1, column)
            left = (row, column - 1)
            right = (row, column + 1)

            if isvalid(*up) and up not in visited and last_visited != 'left':
                last_visited = "up"
                row, column = up
                visit(row, column, visited, nums[1:])
            elif isvalid(*right) and right not in visited:
                last_visited = "right"
                row, column = right
                visit(row, column, visited, nums[1:])
            elif isvalid(*down) and down not in visited:
                last_visited = "down"
                row, column = down
                visit(row, column, visited, nums[1:])
            elif isvalid(*left) and left not in visited:
                last_visited = "left"
                row, column = left
                visit(row, column, visited, nums[1:])
            if isvalid(*up) and up not in visited:
                last_visited = "up"
                row, column = up
                visit(row, column, visited, nums[1:])

        visited = set()
        last_visited = None
        row = 0
        column = 0
        visit(row, column, visited, nums)
        return matrix
