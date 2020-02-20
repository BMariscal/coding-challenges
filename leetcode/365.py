"""
https://aakritty.wordpress.com/2014/02/10/solving-the-water-jug-problem/




"""



class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        a, b = x, y
        if (x == 0 or y == 0) and z == 0:
            return True
        if x == 0 or y == 0 and z > 0:
            return False

        while y:
            r = x % y
            x = y
            y = r
        return z <= a + b and z % x == 0


from math import gcd

"""
gcd = the largest positive integer that divides each of the integers

"""
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x + y:
            return False

        try:
            return z % gcd(x, y) == 0
        except:
            return z == 0

