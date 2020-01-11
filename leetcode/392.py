class Solution:
    def isSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) < len(str1):
            return False
        for i in str2:
            if str1 and i == str1[0]:
                str1 = str1[1:]

        if len(str1) > 0:
            return False
        return True