class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        m = {}

        def jump(i, is_odd):
            if (i, is_odd) in m:
                return m[(i, is_odd)]

            if i == len(A) - 1:
                return True

            if is_odd:
                ind, min_n = None, float("inf")
                for j in range(i + 1, len(A)):
                    if A[j] >= A[i] and A[j] < min_n:
                        min_n = A[j]
                        ind = j
                m[(i, is_odd)] = jump(ind, False) if ind is not None else False
            else:
                ind, max_n = None, -float("inf")
                for j in range(i + 1, len(A)):
                    if A[j] <= A[i] and A[j] > max_n:
                        max_n = A[j]
                        ind = j
                m[(i, is_odd)] = jump(ind, True) if ind is not None else False

            return m[(i, is_odd)]

        count = 0
        for index in range(len(A)):
            if jump(index, True):
                count += 1

        return count