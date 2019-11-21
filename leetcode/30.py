s1 = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
words1 = ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj",
         "lnle", "sefg", "vimw", "bxcb"]


s2 = "barfoothefoobarman"
words2 = ["foo","bar"]


# Brute Force:
# def findSubstring(s, words):
#     w = permutation(words)
#     sett = set()
#     for word in w:
#         sett.add("".join(word))
#     word_list = list(sett)
#     answer_arr = []
#     obj = {}
#     for i in range(len(s)):
#         for j in range(len(s), -1, -1):
#             k = s[i:j]
#             if k in obj:
#                 obj[k].append(i)
#             else:
#                 obj[k] = [i]
#
#     for w in word_list:
#         found = obj.get(w, None)
#         if found != None:
#             if type(found) == list:
#                 for i in found:
#                     answer_arr.append(i)
#             else:
#                 answer_arr.append(found)
#
#     return answer_arr
#
#
# def permutation(lst):
#     print("inside")
#     if len(lst) == 0:
#         return []
#
#     if len(lst) == 1:
#         return [lst]
#
#     l = []
#
#     for i in range(len(lst)):
#         m = lst[i]
#
#         remLst = lst[:i] + lst[i + 1:]
#
#         for p in permutation(remLst):
#             l.append([m] + p)
#     return l


import collections
import copy


def findSubstring(s, words):
    if len(s) < 1 or len(words) < 1:
        return []
    answer = []
    len_str = len(s)
    len_words = len(words)
    len_word = len(words[0])
    total_chars_in_list = len_word * len_words
    counter = collections.Counter(words)

    for i in range(0, len_str - total_chars_in_list + 1, 1):
        temp = copy.deepcopy(counter)
        j = i
        count = len_words

        # Traverse the substring
        while j < i + total_chars_in_list:

            # Extract the word
            word = s[j:j + len_word]

            # If word not found or if frequency of
            # current word is more than required simply break.
            if (word not in counter or
                        temp[word] == 0):
                break

            # Else decrement the count of word
            # from hash_map
            else:
                temp[word] -= 1
                count -= 1
            j += len_word

            # Store the starting index of that substring
        # when all the words in the list are in substring
        if count == 0:
            answer.append(i)
    return answer



# Best:

# def findSubstring(s, words):
#     """
#     :type s: str
#     :type words: List[str]
#     :rtype: List[int]
#     """
#     answer = []
#     m,n,k = len(s), len(words), len(words[0])
#     counter = collections.Counter(words)
#     for i in range(k):
#         temp = copy.deepcopy(counter)
#         start = i
#         for j in range(start, m-k+1, k):
#             word = s[j:j+k]
#             temp[word]-=1
#             while temp[word] < 0:
#                 temp[s[start:start+k]]+=1
#                 start+=k
#             if j+k-start==n*k:
#                 answer.append(start)
#     return answer

a = findSubstring(s1, words1)
print(a)
b = findSubstring(s2, words2)
print(b)
