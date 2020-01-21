
class Solution:
    def minimumDistance(self, W: str) -> int:
        A, B, I, W = {(ord(W[0])-65,-1):0}, {}, math.inf, [ord(w)-65 for w in W]
        def dist(u,v): return abs(u//6 - v//6) + abs(u % 6 - v % 6)
        for w in W[1:]:
            for a in A:
                B[(w,a[1])] = min(B.get((w,a[1]),I), A[a] + dist(a[0],w))
                B[(a[0],w)] = min(B.get((a[0],w),I), A[a] + (a[1] != -1)*dist(a[1],w))
            A, B = B, {}
        return min(A.values())


###################################


from functools import lru_cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        word_length = len(word)

        def distance(char_a: str, char_b: str) -> int:
            if not char_a or not char_b:
                return 0

            index_a = ord(char_a) - 65
            index_b = ord(char_b) - 65

            return abs(index_a // 6 - index_b // 6) + abs(index_a % 6 - index_b % 6)

        @lru_cache(None)
        def find(char_index: int, key_a: str, key_b: str) -> int:
            if char_index == word_length:
                return 0

            char = word[char_index]

            return min(
                find(char_index + 1, key_a, char) + distance(key_b, char),
                find(char_index + 1, char, key_b) + distance(key_a, char)
            )

        return find(0, None, None)