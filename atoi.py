# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-21 15:38:28
LastEditors: jiaqianjing
LastEditTime: 2020-04-21 16:41:55
"""
"""
leetcode 8 字符串转换整数 (atoi)
    https://leetcode-cn.com/problems/string-to-integer-atoi/
    
    请你来实现一个 atoi 函数，使其能将字符串转换成整数。
    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则:
        1. 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
        2. 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
        3. 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。

    思路：
    避免冗余的 if else, 可以使用自动机实现，列出状态迁移的路线
    (状态/条件)  ' '	  +/-	  number	 other
    start	    start	signed	in_number	end
    signed	    end	    end	    in_number	end
    in_number	end	    end	    in_number	end
    end	        end	    end	    end	        end

"""

INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 -1

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.signed = 1
        self.result = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == "in_number":
            self.result = self.result * 10 + int(c)
            self.result = min(self.result, INT_MAX) if self.signed == 1 else min(self.result, -INT_MIN)
        elif self.state == 'signed':
            self.signed = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str):
        automoaton = Automaton()
        for c in str:
            automoaton.get(c)
        return automoaton.signed * automoaton.result


s = Solution()
test = "w-42 3"
res = s.myAtoi(test)
print("res: {}".format(res))

