class Solution:
    def reverse(self, x: int) -> int:
        if len(str(x)) == 1:
            return x
        to_str = str(x)[::-1]
        zero_in = to_str[0]
        if zero_in == '0':
            to_str = to_str[1::]
        if to_str[-1] == '-':
            lst = to_str[:-1]
            to_str = '-' + lst
        num = int(to_str)
        if num < -2147483648 or num > 2147483647:
            return 0

        return num
