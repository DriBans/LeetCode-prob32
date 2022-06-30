# We do not have to use class as we have a standard operators in this case. However, LeetCode requires class function since they are not supported by 
# OOP (Object-Oriented Programming). I will write a separate code without using class later. Let's solve this problem for now. 
# The first two lines of code below are given in leetcode, so we can continue from there.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """ Stack is a function that starts from the end of the list (s: str)."""
        stack = [-1]
        a = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append()
            elif len(stack) == 1:
                stack[0] = 1
            else:
                stack.pop()
                a = max(a, i - stack[-1])
        return
