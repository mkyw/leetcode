'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        f = "({["
        b = ")}]"
        for i in s:
            if i in f:
                stack.append(i)
            elif i in b:
                if not stack:
                    return False
                x = stack.pop()
                if x == '{' and i != '}':
                    return False
                elif x == '(' and i != ')':
                    return False
                elif x == '[' and i != ']':
                    return False
        
        return not stack
        
        print(stack)

s = Solution()
str = "()"
print(s.isValid(str))
str = "()[]{}"
print(s.isValid(str))
str = "(]"
print(s.isValid(str))