class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard_obj = {}

        for k, v in enumerate(keyboard):
            keyboard_obj[v] = k

        total = 0
        total += keyboard_obj[word[0]]
        for i in range(1, len(word)):
            diff = abs(keyboard_obj[word[i - 1]] - keyboard_obj[word[i]])
            total += diff
        return total
