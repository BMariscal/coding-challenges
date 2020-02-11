class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = n
        right = n
        string = ""
        res = []
        return self.dfs(left, right, string, res)

    def dfs(self, left, right, string, res):
        if left:
            self.dfs(left-1, right, string + "(", res)
        if right and left < right:
            self.dfs(left, right-1, string + ")", res)
        if not right:
            res.append(string)
        return res

