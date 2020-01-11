from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        count_stones = Counter(S)

        for e in J:
            stone = count_stones.get(e)
            if stone:
                total+= stone
        return total
