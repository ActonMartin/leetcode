#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (72.87%)
# Likes:    524
# Dislikes: 0
# Total Accepted:    170.2K
# Total Submissions: 232.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_depth = 0
        dpth_count = 1
        de = [(root, depth_count)] # 默认计数为1， 第一层是根节点，深度为1
        while de:
            current_node, depth = de.pop()
            if not current_node.left and not current_node.right:
                max_depth = max(max_depth, depth)
            if current_node.right:
                de.append((current_node.right, depth+1))
            if current_node.left:
                de.append((current_node.left,depth+1))
        return max_depth
# 这一题是我做了112题路径之和 之后又遇到的一个题目，简直是一模一样的套路、
# 但是自己依旧是卡住了，借鉴了其他人的解法，完善了代码，终于可以跑成功了。

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

# @lc code=end

