#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """ 穷举法 """
    def deleteDuplicates(self, head):
        node=head
        while node and node.next:
            if node.val==node.next.val:
                node.next=node.next.next
            else:
                node=node.next
        return head

class Solution1:
    """ 递归法 """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        child = self.deleteDuplicates(head.next)
        if child and head.val == child.val:
            head.next = child.next
            child.next = None
            
        return head
        

# @lc code=end

