class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        new_s = []
        for i in S:
            if new_s and i == "#":
                new_s.pop()
            elif i != "#":
                new_s.append(i)

        new_t = []
        for j in T:
            if new_t and j == "#":
                new_t.pop()
            elif j != "#":
                new_t.append(j)
        return new_s == new_t
