class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """ Stack is a data structure that starts with the ending of the bracket."""
        stack, ans = [-1], 0
        for i in range(len(s)):
            if s[i] == '(': stack.append()
            elif len(stack) == 1: stack[0] = 1
            else:
                stack.pop()
                ans = max(ans, i - stack[-1])
        return