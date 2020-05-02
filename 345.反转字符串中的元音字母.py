#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (49.57%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    33.2K
# Total Submissions: 66.8K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 示例 1:
# 
# 输入: "hello"
# 输出: "holle"
# 
# 
# 示例 2:
# 
# 输入: "leetcode"
# 输出: "leotcede"
# 
# 说明:
# 元音字母不包含字母"y"。
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
            elif s[left] in vowels and s[right] not in vowels:
                left, right = left, right - 1
            elif s[left] not in vowels and s[right] in vowels:
                left, right = left + 1, right
            else:
                left, right = left + 1, right - 1
        s = ''.join(s)
        return s

# @lc code=end

