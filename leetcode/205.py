from collections import defaultdict, OrderedDict
# fun times with collections!
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # return [s.index(i) for i in s] == [t.index(i) for i in t]
        dictS = defaultdict(list)
        for i,e in enumerate(s):
            dictS[e].append(i)
        dictT = defaultdict(list)
        for i,e in enumerate(t):
            dictT[e].append(i)
        t = OrderedDict(sorted(dictT.items(), key=lambda item: len(item[1]), reverse=True))
        s = OrderedDict(sorted(dictS.items(), key=lambda item: len(item[1]), reverse=True))
        return list(s.values() ) == list(t.values() )
