#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]

class AnotherOne():
    def prefix(self, strs):
        s = ""
        for i in zip(*strs):
            if set(i) == 1:
                s += i
            else:
                break
        return s

class SolutionII:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)

# @lc code=end
