
"""
If dp[i][j] == False, it means s[:i] doesn't match p[:j]
If dp[i][j] == True, it means s[:i] matches p[:j]
'.' Matches any single character.
'' Matches zero or more of the preceding element.
s = "aa"
p = "a"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".



s = "aab"
p = "c*a*b"
                 c      *       a      *     b
dp = [
         [True, False, True, False, True, False],
	 a  [False, False, False, True, True, False],
	 a  [False, False, False, False, True, False],
	 b	[False, False, False, False, False, True]]

#  Case 1 p[:j] ==  alphabet or '.'
#  Case 2: p[:j] is '*'
	# Case 2a: p[:j-1] doesn't need a '*' to match the substring s[:i]
	    #1  p[:j-1] ==s[:i]   dp[i][j] =d[i-1][j]
		#2  p[:j-1] == '.'      dp[i][j]=dp[i][j-2]
	# Case 2b: p[:j] needs '*' to match the substring s[:i]




 # about *:
 case 1: 0 preceding element
 case 2: 1 or more preceding element
			   the preceding element could be a '.' or an alpharbet.
			   more proceding element is easy to handle once you use dynamic programming.

"""


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)




class Solution:
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for c in range(1, m + 1):
            if p[c - 1] == '*' and c > 1:
                dp[0][c] = dp[0][c - 2]


        for r in range(1, n + 1):
            for c in range(1, m + 1):
                if p[c - 1] == s[r - 1] or p[c - 1] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif c > 1 and p[c - 1] == '*':
                    if p[c - 2] == '.' or s[r - 1] == p[c - 2]:
                        dp[r][c] = dp[r][c - 2] or dp[r - 1][c]
                    else:
                        dp[r][c] = dp[r][c - 2]
        return dp[n][m]


