class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        answer = [e for e in S if not vowels.get(e, None)]
        return "".join(answer)
