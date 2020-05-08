class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return
        if numRows == 1:
            return [[1]]
        a = [[1, 1] for i in range(numRows)]
        a[0] = [1]
        height = numRows
        previous_row = a[1]
        for x in range(2, height, 1):
            new_arr = []
            for i in range(len(previous_row) - 1):
                num = previous_row[i] + previous_row[i + 1]
                new_arr.append(num)
            a[x] = [a[x][0]] + new_arr + [a[x][-1]]

            previous_row = a[x]

        return a

