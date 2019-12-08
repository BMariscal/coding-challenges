class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for i in range(len(groupSizes)):
            if dic.get(groupSizes[i]):
                dic[groupSizes[i]].append(i)
            else:
                dic[groupSizes[i]] = [i]

        alls = []
        for j, v in dic.items():
            length = len(v)

            if length > j:
                for i in range(0, length, j):
                    alls.append(v[i:j + i])
            else:
                alls.append(v)
        return alls


    