# coding: utf-8

"""
leetcode 6. Z 字形变换
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""
class Solution:
    def convert(self, s, numRows):
        """
        思路：创建 numRows 个数组 array[0]、array[1] ... array[numRows-1]，遍历原始字符串，
        然后依次将字符放入这些数组中，但是因为要 z 型存放，涉及到一个方向的问题，当读取到 
        numRows 个字符的，要往反方向存数据，并放入到 array[numRows-2], 直到又回到 array[0] 的时候
        再次反向，如此反复知道遍历完所有的字符串。
        整个过程就是弹簧一样，往上，往下，如此反复；
        变方向的标志就是，第一行和最后一行，即 array[0] 和 array[numRows-1]
        return: String
        """
        if not s or numRows <= 1:
            return s
        
        s_length = len(s)
        # 创建一个二维数组，存储变形后字符, 这里取 s 长度和 numRows 最小值
        res = [[] for _ in range(min(s_length, numRows))]

        # 创建一个是否要向下的标志位
        is_down = False
        
        # 标记数组的下标
        j = 0

        # 遍历原始字符串
        for i in range(s_length):
            res[j].append(s[i])
            if j == 0:
                is_down = True
            elif j == numRows - 1:
                is_down = False
            j = j + 1 if is_down else j - 1
        
        # 创建一个 string 存储最后的结果
        new_s = ""
        for i in res:
            new_s += ''.join(i)
        
        return new_s



test = "LEETCODEISHIRING"
numRows = 3
s = Solution()
res = s.convert(test, numRows)
print("raw string: {}".format(test))
print("convert string: {}".format(res))



