class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s*2)[1:-1]



# slow solution
import collections
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        str_len = len(s)
        if str_len == 1:
            return False

        word = ""
        o_string = ""
        j = 0
        possible_subs = []
        for i in range(str_len - 1, -1, -1):
            word = s[i] + word
            o_string += s[j]
            j += 1

            if word == o_string:
                possible_subs.append(o_string)
        if len(possible_subs) > 1:
            possible_subs.pop()
        if possible_subs[0] == s:
            return False
        final_word = ""
        k = 0

        while len(possible_subs) > 0:
            word = possible_subs[k]
            for j in range(0, str_len, len(word)):
                final_word += word
            if final_word == s:
                return True
            possible_subs.pop(k)
            final_word = ""
        return False






