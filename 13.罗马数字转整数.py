#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d={'M':1000,'CM':900,'D':500,'CD':400,'C':100,
            'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,
            'IV':4,'I':1}
        res,i=0,0
        while i<len(s)-1:
            if d[s[i]]<d[s[i+1]]:
                res+=d[s[i:i+2]]
                i+=2
            else:
                res+=d[s[i]]
                i+=1
        return res if i>=len(s) else res+d[s[-1]]

# @lc code=end

