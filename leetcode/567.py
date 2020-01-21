from collections import Counter


class Solution:
    def checkInclusion(self, pattern: str, s: str) -> bool:
        pattern_counter = Counter(pattern)
        start = 0
        match = 0

        for end in range(len(s)):
            if s[end] in pattern_counter:
                pattern_counter[s[end]] -= 1

                if pattern_counter[s[end]] == 0:
                    match += 1
            if match == len(pattern_counter):
                return True

            if end >= len(pattern) - 1:
                left_most = s[start]
                start += 1
                if left_most in pattern_counter:
                    if pattern_counter[left_most] == 0:
                        match -= 1
                    pattern_counter[left_most] += 1

        return False


