NUMS_TO_LETTER = {}
import string


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        k = 2
        j = 3
        alphabet = string.ascii_lowercase
        for i in range(0, len(alphabet), j):
            if k < 10:
                if k == 7 or k == 9:
                    j = 4
                    NUMS_TO_LETTER[str(k)] = alphabet[i:i + j]
                if k == 8:
                    j = 3
                    i += 1

                    NUMS_TO_LETTER[str(k)] = alphabet[i:i + j]
                if k == 9:
                    i += 1
                    NUMS_TO_LETTER[str(k)] = alphabet[i:]
                else:
                    NUMS_TO_LETTER[str(k)] = alphabet[i:i + j]
                k += 1
        res = []
        st = ""
        self.dfs(digits, res, st)
        return res

    def dfs(self, digits, res, st):
        if len(digits) == 0:
            res.append(st)
        else:

            for letter in NUMS_TO_LETTER[digits[0]]:
                self.dfs(digits[1:], res, st + letter)






