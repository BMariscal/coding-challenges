
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        return collections.Counter(s) == collections.Counter(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_hash = 0
        t_hash = 0
        if s_len == 0 and t_len == 0:
            return True
        if s_len < t_len or t_len < s_len:
            return False

        for i in range(t_len):
            s_hash += hash(s[i])
            t_hash += hash(t[i])

        if s_hash == t_hash:
            return True
        return False
