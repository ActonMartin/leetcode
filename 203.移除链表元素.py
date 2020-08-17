#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head: head.next = self.removeElements(head.next, val)
        return head.next if head and head.val == val else head

class Solution:
    """ 65/65 cases passed (84 ms)
Your runtime beats 38.71 % of python3 submissions
Your memory usage beats 8.86 % of python3 submissions (16.9 MB) """
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next
# @lc code=end

