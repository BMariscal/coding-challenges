class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # create hashmap of order string, letter as key, index as value
        # sort word in words based on index value in hashmap

        d = {}
        for i in range(len(order)):
            d[order[i]] = i

        for idx in range(len(words) - 1):
            word1 = words[idx]
            word2 = words[idx + 1]

            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if d[word1[k]] > d[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True


