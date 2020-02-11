class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not target or target < min(candidates):
            return []

        ans = []
        for i in range(len(candidates)):
            num = candidates[i]
            if num == target:
                ans.append([target])
            else:
                res = self.combinationSum(candidates[i:], target - num)
                ans += [[num] + item for item in res]
        return ans