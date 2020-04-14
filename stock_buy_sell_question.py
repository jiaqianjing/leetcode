"""
Descripttion:  https://cloud.tencent.com/developer/article/1426372
version: 
Author: jiaqianjing
Date: 2020-03-01 12:38:36
LastEditors: jiaqianjing
LastEditTime: 2020-03-01 13:14:14
"""


class Solution:
    def max_profit_01(self, prices):
        """
        leetcode 121: 只能买卖一次
        """
        if len(prices) <= 1:
            return 0
        # 第一天
        buy = -prices[0]
        sell = 0
        
        # FOCUS index=1
        for i in range(1, len(prices)):
            buy = max(buy, -prices[i])
            sell = max(sell, prices[i] + buy)

        return sell

    def max_profit_02(self, prices):
        """
        leetcode 122: 多次买卖一支股票 (你不能同时参与多笔交易,如：连续买，只能买卖各一次)
        """
        if len(prices) <= 1:
            return 0

        # 第一天
        buy = -prices[0]
        sell = 0
        
        # FOCUS index=1
        for i in range(1, len(prices)):
            buy = max(buy, sell-prices[i])
            sell = max(sell, buy + prices[i])
        return sell

    def max_profit_03(prices):
        """
        leetcode 123: 你最多可以完成 两笔 交易, (你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票))
        """
        if len(prices) <= 1:
            return 0
        # 初始化
        first_buy = float('-inf')
        first_sell = 0
        sec_buy = float('-inf')
        sec_sell = 0
        # FOCUS index=0
        for i in range(len(prices)):
            first_buy = max(first_buy, -prices[i])
            first_sell = max(first_sell, first_buy + prices[i])
            sec_buy = max(sec_buy, first_sell-prices[i])
            sec_sell = max(sec_sell, sec_buy+prices[i])

        return sec_sell

            
