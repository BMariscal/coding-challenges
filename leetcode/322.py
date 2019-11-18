"""

F(3)=min{F(3−c1),F(3−c2),F(3−c3)}+1
=min{F(3−1),F(3−2),F(3−3)}+1
=min{F(2),F(1),F(0)}+1
=min{1,1,0}+1
=1
​
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0

        for c in coins:  # 2
            for i in range(c, amount + 1):  # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
                min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)

        return min_coins[-1] if min_coins[-1] != float('inf') else -1