# coding:utf-8
import copy


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def twoSum(self, nums, target):
        i = 0
        while i < len(nums):
            r = target - nums[i]
            nums_follows = nums[i+1:]
            if r in nums_follows:
                return [i, nums_follows.index(r) + i + 1]
            i += 1

        return "no solutions"

    def quick_sort(self, nums, low, high):
        """
        partition-exchange sort or quick sort
        """
        def _partition(nums, low, high):
            # 取最右边最为基准值
            pivot = nums[low]

            # 保证基准值的位置左边都比他大，右边都比他小
            while low < high:
                while low < high and nums[high] >= pivot:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] < pivot:
                    low += 1
                nums[high] = nums[low]
            # low 就是基准值在数组中的新位置
            nums[low] = pivot
            return low

        if low >= high:
            return
        k = _partition(nums, low, high)
        self.quick_sort(nums, low, k)
        self.quick_sort(nums, k+1, high)

    def merge_sort(self, nums):
        def _merge(left, right):
            i = 0
            j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return _merge(left, right)

    def bucket_sort(self, nums):
        """
        分桶排序，初始化一个 M 数组,初始值 0（桶）
        分别把待排序的数字出现的次数放到对应的下标
        """
        bucket = [0] * 11

        for n in nums:
            bucket[n] += 1
        result = []
        for i, k in enumerate(bucket):
            if k > 0:
                for temp in range(k):
                    result.append(i)
        return result

    def max_subsequence_sum(self, nums):
        """
        最大子序列和，动态规划， O(n)
        """
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]

        sum_add = 0
        # 负无穷大
        max_sum = float('-inf')
        for i in range(nums_len):
            temp = sum_add + nums[i]
            if temp < nums[i]:
                sum_add = nums[i]
            else:
                sum_add = temp
            if max_sum < sum_add:
                max_sum = sum_add
        return max_sum

    def merge_two_listnode(self, l1, l2):
        """
        合并两个有序链表
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1

        l = []
        while l1:
            l.append(l1.val)
            l1 = l1.next

        while l2:
            l.append(l2.val)
            l2 = l2.next

        l.sort()
        new_l = ListNode(l[0])
        head_l = new_l
        # FOCUS
        for i in range(1, len(l)):
            new_l.next = ListNode(l[i])
            new_l = new_l.next

        new_l.next = None
        return head_l

    def longestPalindRome(self, s):
        """
        最长回文字符串: https://www.jianshu.com/p/035474c1c0a0;
                      https://blog.csdn.net/weixin_37675458/article/details/85260054
        思路：[动态规划]
        1. 头尾相同，最长回文字符串一定是去头去尾之后的部分最长回文字符串加上头尾
        2. 如果头尾不同，最长回文字符串 = max(去头部分的最长回文字符串, 去尾部分的最长回文字符串）
        """
        str_len = len(s)
        start = 0
        max_len = 0
        for i in range(str_len):
            if i - max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i - max_len
                max_len += 1

        return s[start:start + max_len]


if __name__ == "__main__":
    s = Solution()
    print("two nums sum: %s " % s.twoSum([1, 2, 3, 4, 5], 5))

    a_raw = [2, 4, 2, 5]
    a = copy.deepcopy(a_raw)
    print("raw nums: %s" % a_raw)
    s.quick_sort(a, 0, len(a)-1)
    print("quick sort: %s" % a)
    print("merge sort: %s" % s.merge_sort(a_raw))
    print("bucket sort: %s" % s.bucket_sort(a_raw))

    a = [1, 2, 7, -8, 3, -9, 2, 3, 4]
    a = [1]
    print("%s 最大子序列和: %s" % (a, s.max_subsequence_sum(a)))
