#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
'''
第三种方法：DP动态规划，第i天只有两种状态，不持有或持有股票，
当天不持有股票的状态可能来自昨天卖出或者昨天也不持有，
同理，当天持有股票的状态可能来自昨天买入或者昨天也持有中，
取最后一天的不持有股票状态就是问题的解
'''
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        # dp[i][0]表示第i天不持有股票, dp[i][1]表示第i天持有股票
        dp[0][0], dp[0][1] = 0, - prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(0,len(prices)-1):
            if prices[i] >= prices[i+1]:
                peak = 0
                valley = 0
            else:
                peak = prices[i+1]
                valley = prices[i]
            gap = peak - valley
            max_profit += gap
        print(max_profit)
        return max_profit
# @lc code=end

