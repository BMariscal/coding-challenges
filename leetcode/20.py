class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for element in s:
            if element == '(' or element == '{' or element == '[':
                stack.append(element)
            elif len(stack) <= 0:
                return False
            elif element == ')' and stack.pop() != '(':
                return False
            elif element == '}' and stack.pop() != '{':
                return False
            elif element == ']' and stack.pop() != '[':
                return False
        if len(stack) == 0:
            return True

        return False