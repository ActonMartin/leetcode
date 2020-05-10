#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (44.54%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    74.4K
# Total Submissions: 166.5K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 案例:
# 
# 
# s = "leetcode"
# 返回 0.
# 
# s = "loveleetcode",
# 返回 2.
# 
# 
# 
# 
# 注意事项：您可以假定该字符串只包含小写字母。
# 
#

# @lc code=start\
from collections import defaultdict
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        if s is '':
            return -1
        hash_table = defaultdict(int)
        for index, val in enumerate(s):
            hash_table[val] += 1
        ss =  sorted(hash_table.items(), key= lambda x: x[1])
        for j in ss:
            if j[1] == 1:
                target = j[0]
                break
            else:
                return -1
        for index, val in enumerate(s):
            if val == target:
                return index
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        lis = list(s)
        setlis = sorted(set(lis),key = lis.index)
        print(setlis)
        for i in setlis:
            if i not in s.replace(i,'A',1):
                print(s)
                return lis.index(i)
        return -1


# @lc code=end

