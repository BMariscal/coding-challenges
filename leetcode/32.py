class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maximum = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                # if the character is ')'
                stack.pop()
                if not stack:
                    #  If stack is empty, push current index as base for next
                    # valid substring.
                    stack.append(i)
                else:
                    # If stack is not empty, then find length of current valid
                    #       substring by taking difference between current index and
                    #       top of the stack. If current length is more than result,
                    #       then update the result.
                    maximum = max(maximum, i - stack[-1])
        return maximum





class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = [0] * (len(s) + 1)

        for i, element in enumerate(s):
            if element == '(':
                stack.append(i)
            else:
                if stack:
                    popped = stack.pop()
                    dp[i + 1] = dp[popped] + i - popped + 1

        return max(dp)