from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        new_guess = ""
        new_secret = ""
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                A += 1
            else:
                new_guess += guess[i]
                new_secret += secret[i]

        dic = Counter(new_secret)
        for i in range(len(new_guess)):
            if new_guess[i] in dic and dic[new_guess[i]] > 0:
                B += 1
                dic[new_guess[i]] -= 1

        return "{}A{}B".format(A, B)


