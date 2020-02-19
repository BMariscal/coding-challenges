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
