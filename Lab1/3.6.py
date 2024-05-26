from itertools import combinations
def powerset(V):
    result=[]
    n=len(V)
    for sublen in range (n+1):   #i从0到n，子集从空集到全集
        #第一重循环，遍历子集元素个数
        for i in combinations(V,sublen):#第二重循环，遍历迭代器
            result.append(set(i))
    #combination将会返回迭代器,将其类型转换为set类型
    return result

V1=set(input().split(','))
#对于输入要进行处理，这边用split把空格过滤掉
print(powerset(V1))
