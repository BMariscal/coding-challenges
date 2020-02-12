L = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
VOWELS = {}
for l in L:
    VOWELS[l] = l


class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = S.split()
        res = ""
        aces = "a"
        for i in range(len(s)):
            w = s[i]
            if w[0] in VOWELS:
                s[i] = w + "ma"
            else:
                temp = w[0]
                s[i] = w[1:] + temp + "ma"

            s[i] = s[i] + (aces * (i + 1))

        return " ".join(s)
