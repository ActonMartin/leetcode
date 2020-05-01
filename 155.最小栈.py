#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []


    def push(self, x: int) -> None:
        return self.minStack.append(x)

    def pop(self) -> None:
        return self.minStack.pop()


    def top(self) -> int:
        if not self.is_empty():
            return self.minStack[-1]

    def getMin(self) -> int:
        return min(self.minStack)
    
    def is_empty(self):
        return self.minStack == []


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.minnum = None

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = None
        self.next = None


    def push(self, x: int) -> None:
        p = Node(x)
        p.next = self.next
        self.next = p
        if p.next:
            p.minnum = min(x, p.next.minnum)
        else:
            p.minnum = x 


    def pop(self) -> None:
        tmp = self.next
        if tmp != None:
            self.next = tmp.next
        return 


    def top(self) -> int:
        if self.next != None:
            return self.next.data
        return None


    def getMin(self) -> int:
        p = self.next
        return p.minnum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

