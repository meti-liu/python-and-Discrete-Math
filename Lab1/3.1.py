import random

s1 = {1, 2, 3, 4}
s2 = {'a', 'b', 'c', 'd'}


def createset(m, n):
    return set(random.sample(range(m), n))
    # 从0-m-1中生成n个数，set保证不重复，满足集合的互异性
set1 =createset(10,5)
print(set1)