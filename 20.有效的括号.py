#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False 
        
class Solution:
    def isValid(self, s: str) -> bool:
        ss = Stack()
        is_balanced = True
        index = 0

        while index < len(s) and is_balanced:
            paren = s[index]
            if paren in "([{":
                ss.push(paren)
            else:
                if ss.is_empty():
                    is_balanced = False
                else:
                    top = ss.pop()
                    if not is_match(top, paren):
                        is_balanced = False
            index += 1

        if ss.is_empty() and is_balanced:
            return True
        else:
            return False


class SSolution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            elif len(stack) == 0 or mapping[char] != stack.pop():
                return False
        return len(stack) == 0

  
# @lc code=end

