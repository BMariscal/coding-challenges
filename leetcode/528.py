
"""

The idea is simple -

Initialize an array containing weights
Do a binary search between 0 and the sum of all weights in your init
Note: I had trouble getting this problem accepted because I was using random.randInt instead of random.uniform

"""


class Solution:
    def __init__(self, w: List[int]):
        self.probs = []
        self.s = 0
        for n in w:
            self.probs.append((self.s, self.s + n))
            self.s += n
        self.m = 0
        self.c = {}

    def pickIndex(self) -> int:
        r = random.uniform(0, self.s)
        b = self.bin_search(self.probs, 0, len(self.probs), r)
        self.m += 1
        self.c[b] = self.c.get(b, 0) + 1

        return b

    def bin_search(self, arr, a, c, n):
        if a > c:
            return -1
        b = int((a + c) / 2)
        if arr[b][0] <= n <= arr[b][1]:
            return b
        if n > arr[b][1]:
            return self.bin_search(arr, b + 1, c, n)
        return self.bin_search(arr, a, b - 1, n)


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()