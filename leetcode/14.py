class Solution:
    def longestCommonPrefix(self, string: List[str]) -> str:
        if not string:
            return ""
        minimum = min(string)
        maximum = max(string)
        i = 0
        for i in range(min(len(minimum), len(maximum))):
            if minimum[i] != maximum[i]:
                break
        else:
            i += 1
        return minimum[:i]
