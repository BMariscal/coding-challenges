class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        answer = {}
        for word in strs:
            word_hash = hash("".join(sorted(word)))
            if not answer.get(word_hash):
                answer[word_hash] = [word]
            else:
                answer[word_hash].append(word)

        return answer.values()

