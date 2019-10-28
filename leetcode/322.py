"""

F(3)=min{F(3−c1),F(3−c2),F(3−c3)}+1
=min{F(3−1),F(3−2),F(3−3)}+1
=min{F(2),F(1),F(0)}+1
=min{1,1,0}+1
=1
​
"""




def coinChange(coins, amount):
    if amount < 1:
        return 0

    all_combos = [amount + 1] * (amount+1)
    all_combos[0] = 0

    for amt in range(1, amount +1):
        for coin in coins:
            if amt - coin >= 0 :
                all_combos[amt] = min(all_combos[amt], 1 + all_combos[amt - coin])

    if all_combos[amt] > amount:
        return -1

    return all_combos[amt]