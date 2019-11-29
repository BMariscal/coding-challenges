class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_s = len(s)
        length_p = len(p)
        if length_s < length_p:
            return []

        s_hash = 0
        p_hash = 0
        result = []

        for i in range(length_p):
            s_hash += hash(s[i])
            p_hash += hash(p[i])

        if s_hash == p_hash:
            result.append(0)

        for j in range(length_p, length_s):
            s_hash += hash(s[j]) - hash(s[j - length_p])

            if s_hash == p_hash:
                result.append(j - length_p + 1)
        return result

