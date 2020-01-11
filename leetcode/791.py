from collections import OrderedDict
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        letters_in_S = ""
        d = OrderedDict()
        for i in range(len(T)):
            j = T[i]
            if j in d:
                d[j].append(i)
            else:
                d[j] = [i]
        for letter in S:
            letter_exists = d.get(letter)
            if letter_exists:
                for _ in letter_exists:
                    letters_in_S+=letter
                del d[letter]

        remaining_dict_letters = ""
        for v in d:
            for i in d[v]:
                remaining_dict_letters+=v
        return letters_in_S + "".join(sorted(remaining_dict_letters))

# class Solution:
#     def customSortString(self, S: str, T: str) -> str:
#         count = collections.Counter(T)
#         res = []
#         for i in S:
#             res.append(i * count[i])
#             count[i] = 0
#         for i in count:
#             res.append(i * count[i])
#         return "".join(res)