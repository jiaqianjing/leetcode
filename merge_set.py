# coding: utf-8
"""
Descripttion: 
version: 
Author: jiaqianjing
Date: 2020-04-07 15:18:45
LastEditors: jiaqianjing
LastEditTime: 2020-04-14 18:50:16
"""

"""
问题描述：合并具有交集的集合 (连通分量算法)
相关链接：
    http://www.cocoachina.com/articles/90406
    https://www.cnblogs.com/betabear/p/11687245.html
头条、美团面试题：
给定一些线段信息，如 (a, b) (a, c) (e, f), 组成新的线段 (a, b, c) (e, f)
"""
class Solution:
    def merge_set_list(self, l):
        # 根据输入的 list，转成一组由 frozenset 的集合
        pool = map(frozenset, l)
        # 创建一个 list 存转换后结果
        result = []
        while pool:
            result.append(set(pool.pop()))
            # 保证遍历到最后一组 frozenset
            while True:
                for i in pool:
                    # 判断是否有交集
                    if result[-1] & i:
                        # 取并集
                        result[-1] |= i
                        pool.remove(i)
                        break
                else:
                    break
        return result

test = [{'a', 'b'}, {'a', 'c'}, {'e', 'f'}, {'c', 'd'}]
print("raw test: {}".format(test))
s = Solution()
res = s.merge_set_list(test)
print("res: {}".format(res))

