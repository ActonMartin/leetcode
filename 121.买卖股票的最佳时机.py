#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            compare_profit = price - min_price
            max_profit = max(max_profit, compare_profit)
        return max_profit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for cur in range(len(prices)-1):
            for sec in range(cur+1, len(prices)):
                if prices[sec] - prices[cur]> max_profit:
                    max_profit = prices[sec] - prices[cur]
        return max_profit
        
# @lc code=end

