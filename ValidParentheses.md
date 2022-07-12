Valid Parentheses is "when every opening bracket must have a matching closing bracket of the same type" and (2*) the brackets should be closed in a correct order.

Let's have a code example.
Given a string containing a simple parantheses, square parantheses and curly parantheses -- (), [], {} respectively.
We will see if the string is valid or not.

(1*) We will determine if this condition is met..... which is when every opening bracket must have a matching closing bracket of the same type.

There are two approaches for this concept, but we will use stack approach. Imagine you are given some layers one by one and you are asked to stack them in an order.
After all, stack in data structure is similar to those stacks of layers.

Let's look at the steps that will help us understand better as to what to do:
- Iterate the given string
- If we start face-to-face with an opening bracket, push it onto the stack.
- If we get a closing bracket, then check the element on the top of the stack. If the top element is '(' then pop the top element. Else, the string is invalid.
- In the end, if the stack is empty then given string is valid, otherwise invalid.

We have this term LIFO (Last In First Out), meaning when you can add elements to the top of the stack and remove them from the top of the stack.

(2*) The brackets should be closed in a correct order. We will determine if the string is valid with this condition.

A string can be valid if inside every pair of opening and closing brackets lies a valid string od parentheses.

- For string {({}())} to be valid, its substring ({}()) has to be valid.
- For string ({}()) to be valid, its substrings {}() have to be valid.

Above are the examples of validity of substrings. We can determine that the string is valid only after a valid of its substring.

Note: We can iterate from either left to right or right to left, it just has to be in an order. 
