class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        width = len(m[0])
        height = len(m)
        x_axis = []
        y_axis = []

        for x in range(height):
            for y in range(width):
                if m[x][y] == 0:
                    x_axis.append(x)
                    y_axis.append(y)

        for i in x_axis:
            for j in range(width):
                m[i][j] = 0

        for j in range(height):
            for i in y_axis:
                m[j][i] = 0






