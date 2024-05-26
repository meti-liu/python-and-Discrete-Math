import random



def combine(R, S):
    """返回R∪S"""
    return R.union(S)

def intersection(R, S):
    """返回R∩S"""
    return R.intersection(S)

def subtraction(R, S):
    """返回R-S"""
    return R.difference(S)

def xor(R, S):
    """返回R⊕S"""
    return R.symmetric_difference(S)

def composite(R, S):
    """返回R∘S"""
    return set((x, z) for x, y1 in R for y2, z in S if y1 == y2)

def powern(R, n):
    """返回R的n次幂"""
    if n == 0:
        return {(x, x) for x, y in R}
    result = R
    for _ in range(n - 1):
        result = composite(result, R)
    return result

R={(4, 4), (0, 1), (2, 1), (0, 0), (3, 1), (1, 1), (2, 0), (3, 0), (3, 3), (1, 0)}
S={(4, 4), (0, 1), (4, 0), (1, 2), (4, 3), (3, 1), (1, 4), (0, 2), (1, 0), (4, 1)}

# 执行各种集合操作
R_union_S = combine(R, S)
R_intersection_S = intersection(R, S)
R_subtraction_S = subtraction(R, S)
R_xor_S = xor(R, S)
R_composite_S = composite(R, S)
R_power_2 = powern(R, 2)

# 输出结果
print(f"关系 R：{R}")
print(f"关系 S：{S}")
print(f"R ∪ S：{R_union_S}")
print(f"R ∩ S：{R_intersection_S}")
print(f"R - S：{R_subtraction_S}")
print(f"R ⊕ S：{R_xor_S}")
print(f"R ∘ S：{R_composite_S}")
print(f"R^2：{R_power_2}")
