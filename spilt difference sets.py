# Singer Difference Sets
N = 40
K = 13
Zn = set(range(N))
u = {0, 1, 3, 5, 9, 15, 22, 25, 26, 27, 34, 35, 38}
u_hat = Zn - u

# #Twin-Primes
# N = 15
# K = 8
# Zn = set(range(N))
# u = {3, 6, 7, 9, 11, 12, 13, 14}
# u_hat = Zn - u

# # Singer Difference Sets 2
# N = 57
# K = 8
# Zn = set(range(N))
# u = {1, 6, 7, 9, 19, 38, 38, 42, 49}
# u_hat = Zn - u


# Calculate sumset
def sumset(set1, set2, mod):
    sumset = set()
    for item1 in set1:
        for item2 in set2:
            add = item1 + item2
            if add<0 or add>=mod:
                add = add % mod
            sumset.add(add)
    return sumset


def find_difference(set_u, N):
    """
    set_u:差集中的取值
    N:总数
    """
    diff_dict = {}
    for i in range(1, N):
        diff_list = set()
        # 双重循环，让集合内任意两个数相减
        for num1 in set_u:
            for num2 in set_u:
                difference = num1 - num2
                if difference == i or difference + N == i:
                    diff_list.add(num2)
        diff_dict[i] = diff_list

    # 返回值是字典
    return diff_dict

def find_maxbanlanced_intersection(diff_dict):
    """
    diff_dict:差集拆分后的字典，key是值，values是集合
    """
    maximum = -1  # 统计重叠的最大值
    keys = list(diff_dict.keys())
    for i in range(1, len(keys)+1):
        value1 = diff_dict[i]

        for j in range(1, len(keys)+1):
            value2 = diff_dict[j]
            intersection = value1 & value2
            maximum = len(intersection) if maximum<len(intersection) else maximum

    index = dict()

    for number in range(maximum, 0, -1): #只基于第一个集合找交集
        print('number is ',number)
        for i in range(1, len(keys)+1):
            value1 = diff_dict[i]
            intersection1 = set()
            overlap = value1
            if i != j:
                for j in range(1, len(keys)+1):
                    value2 = diff_dict[j]
                    overlap = overlap & value2
                    if len(overlap) == number:
                        intersection2 = tuple(overlap) #用元组存intersection2，后续会作为intersection1集合中的元素、index字典中的键
                    cross = len(intersection2)
                    if cross == number:
                        if intersection2 not in intersection1:
                            intersection1.add(intersection2)
                            index[intersection2] = set([0, i, j])
                        elif intersection2 in intersection1:
                            index[intersection2].add(j)


    return index



diff = find_difference(u_hat, N)
index = find_maxbanlanced_intersection(diff)
for key,value in index.items():
    print('{key}:{value}'.format(key = key, value = value))