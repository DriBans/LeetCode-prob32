# We do not have to use class as we have a standard operators in this case. However, LeetCode requires class function since they are not supported by 
# OOP (Object-Oriented Programming). I will write a separate code without using class later. Let's solve this problem for now. 
# The first two lines of code below are given in leetcode, so we can continue from there.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """Stack is a function that starts from the end of the list (s: str)."""

        #initialize the stack by -1 which means from the right to left.
        stack = [-1]

        #Stores the length of the longest bracket
        a = 0

        #iterate over the characters of the strings.
        for i in range(len(s)):

            # If the first character is an opening bracket, then push it onto the stack
            if s[i] == '(':
                stack.append()
            elif len(stack) == 1:
                stack[0] = 1
            
            # If the first character is a closing bracket, then pop the top element.
            else:
                stack.pop()
                a = max(a, i - stack[-1])
        return


from collections import deque
def longestValid(s):
    if not s: return 0

    stack = deque()
    stack.append(-1)
    a = 0
    
    for i, x in enumerate(s):
        if x == '(':
            stack.append(i)
        else:
            stack.pop()
            
            # If the stack is empty, then push the index into the stack.
            if not stack:
                stack.append(i)
                continue
        current_length = i - stack[-1]
        if a < current_length:
            a = current_length
    return a

if __name__ == '__main__':
    print(longestValid('((()()'))
    print(longestValid('(((()'))
