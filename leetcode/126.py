from string import ascii_lowercase


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree = collections.defaultdict(set)
        words = set(wordList)
        n = len(beginWord)
        if endWord not in wordList:
            return []

        found = False
        bq = {beginWord}
        eq = {endWord}
        nq = set()
        rev = False

        while bq and not found:
            words -= set(bq)
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in ascii_lowercase]:
                    if y in words:
                        if y in eq:
                            found = True
                        else:
                            nq.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            bq = nq
            nq = set()
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev

        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]

        return bt(beginWord)