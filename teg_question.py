# coding:utf-8


def check_param_type(arg_type, *args):
    """
    检查函数参数类型, 如是否是 list, arg_type=list
    """
    if args is None:
        return
    for arg in args:
        if isinstance(arg, arg_type):
            continue
        else:
            raise Exception("arg: {} is not type: {}".format(arg, arg_type))


def quick_sort(a, low, high):
    """
    快排也称为：划分交换排序，partition-exchange sort
    时间复杂度：nlogn (理想情况，完全二叉树)  n^2 (最坏情况，链表，斜二叉树)
    空间复杂度：虽然快排，是原地排序,只需要引用常数级的变量，但是有递归操作，因此其空间复杂度也是和其树的深度有关，
        logn (理想情况) n^2 (最坏情况)

    """
    def partition(a, low, high):
        # 设置基准值 pivot
        pivot = a[low]
        while low < high:
            while low < high and a[high] >= pivot:
                high -=1
            a[low] = a[high]
            while low < high and a[low] < pivot:
                low +=1
            a[high] = a[low]
        
        a[low] = pivot
        print("low: {}, pivot: {}".format(low, pivot))
        return low

    if low >= high:
        # 保持分组的数组顺序不变，跳出递归
        return
    k = partition(a, low, high)
    quick_sort(a, low, k)
    quick_sort(a, k+1, high)


def merge_sort(a):
    """
    时间复杂度: nlogn
    空间复杂度: n
    """
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

    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return _merge(left, right)


def question_one(a, b, c):
    """
    name: jiaqianjing
    description: 求 A 第 3 大的数 + B 第 4 小的数 + C 第 5 大的数结果, 不存在则为 0
    param {list a, list b, list c}
    return: long or int
    """
    check_param_type(list, a, b, c)
    result = 0
    if len(a) < 3 or len(b) < 4 or len(c) < 5:
        return result
    else:
        try:
            # 降序排列, list.sort() 内部采用 Timesort, 时间最坏复杂度: nlogn, 空间复杂度：n
            # list.sort(): https://www.cnblogs.com/clement-jiao/p/9243066.html
            a.sort(reverse=True)
            # 升序排列 list
            b.sort(reverse=False)
            # 降序排列
            c.sort(reverse=True)
            result = a[2] + b[3] + c[4]
        except Exception as e:
            print("[warn] disaster happend, e: {}".format(e))
    return result


def question_two(a, n, m):
    """
    name: jiaqianjing
    description: 数组A[n], 设数组 A 的子集为连续 m 个数，即 A[0:m-1] , A[1:m] … A[n-m+1:n] 子集的和为这 m 个数相加，
    求和最大的子集(有多个则输出多个)
    param: a[n], n, m
    return: list[list[int]]
    """
    check_param_type(list, a)
    if len(a)-1 != n:
        raise ValueError("n is not equal a length, please check your param n")

    def _sum_list(temp):
        sum = 0
        for t in temp:
            sum += t
        return sum

    i = 0
    # 用于存放子序列的和，以及对应的 index
    temp_dict = {}
    while(i+m-1 <= n):
        if a[i] < 0 and a[i] < a[i+m]:
            i+=1
            continue
        sub_sum_list = _sum_list(a[i:i+m])
        if sub_sum_list not in temp_dict.keys():
            temp_dict[sub_sum_list] = [i]
        else:
            temp_dict[sub_sum_list].append(i)
        i += 1

    indexes = temp_dict[max(temp_dict.keys())]
    result = []
    for index in indexes:
        result.append(a[index:index+m])

    return result


def question_three_new(a, b, c):
    """
    """
    check_param_type(list, a, b, c)
    # 创建 a 数组的 map; 其中 key 记录原始数据，value 记录原始数据的顺序（如果有重复的数据，仅记录第一次出现的位置）
    a_dict = {}
    for i, v in enumerate(a):
        if v in a_dict.keys():
            continue
        a_dict[v] = i

    # 求出三个组的交集
    temp_res = list(set(a).intersection(b, c))
    if not temp_res:
        return []

    # 构建交集在数组 a 的顺序组成字典，key 为交集的数据，value 为原始数据所在的位置
    res_dict = {}
    for i in temp_res:
        res_dict[i] = a_dict.get(i)

    # 将字典按照 value 排序，即可得到交集在原始数据的顺序
    return dict(sorted(res_dict.items(), key=lambda x: x[1])).keys()


def question_three(a, b, c):
    """
    name: jiaqianjing
    description: 给定三个数组 A, B, C 找到它们的有序交集 S, 如:
        A[] = [1, 2, 3,4]
        B[] = [1, 2, 4]
        C[] = [4, 3, 1]
        S[] = [1,4]
    param {list a, list b, list c}
    return: list[int]
    """
    check_param_type(list, a, b, c)
    # 不能保证有序
    # return list(set(a).intersection(b, c))

    def _intersection(temp_a, temp_b):
        """
        求两个 list 的有序交集
        """
        temp_a.sort()
        temp_b.sort()
        res = []
        i = 0
        j = 0
        while(i < len(temp_a) and j < len(temp_b)):
            if temp_a[i] < temp_b[j]:
                i += 1
            elif temp_a[i] > temp_b[j]:
                j += 1
            else:
                res.append(temp_a[i])
                i += 1
                j += 1
        return res

    return _intersection(_intersection(a, b), c)


if __name__ == "__main__":
    a = [1, 8, 3, 6, 5, 5, 7]
    b = [3, 2, 4, 1, 6, 6]
    c = [1, 2, 3, 4, 5, 6]
    # print("raw data: a: {}, b: {}, c: {}".format(a, b, c))
    print("a: %s" % a)
    print("a merge sort: %s" % merge_sort(a))
    # a = [4,3,2,6,5,3,2]
    # print("raw a: {}".format(a))
    # quick_sort(a, 0, len(a)-1)
    # print("a quick sort: %s" % a)

    # a = [-1, 2, -8, 3, 2]
    # print a
    # maxVal, x, y = violence(a)
    # print(maxVal, (x, y))

    # res_01 = question_one(a, b, c)
    # print("res_01: {}".format(res_01))

    # res_02 = question_two(a, len(a)-1, 3)
    # print("res_02: {}".format(res_02))

    # res_03 = question_three_new(a, b, c)
    # print("res_03: {}".format(res_03))
