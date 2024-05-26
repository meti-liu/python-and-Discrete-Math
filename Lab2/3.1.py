def Ixset(R):
    elements=set()
    for (x, y) in R:
        elements.add(x)
        elements.add(y)
    return {(x, x) for x in elements}

def isreflexive(R):
    if Ixset(R)<=R:
        return True
    else:
        return False

def isirreflexive(R):
    if Ixset(R)&R==set():#交集为空集
        return True
    else:
        return False

# 完全自反关系
R1 = {(1, 1), (2, 2), (3, 3)}

# 部分自反关系
R2 = {(1, 1), (2, 2), (1, 2), (2, 3)}

# 非自反关系
R3 = {(1, 2), (2, 1), (2, 3)}

# 含自反与非自反元素的关系
R4 = {(1, 1), (2, 2), (1, 2), (2, 3), (3, 1)}

# 执行测试
print("R1 自反性:", isreflexive(R1))  # 应返回 True
print("R1 反自反性:", isirreflexive(R1))  # 应返回 False

print("R2 自反性:", isreflexive(R2))  # 应返回 False
print("R2 反自反性:", isirreflexive(R2))  # 应返回 False

print("R3 自反性:", isreflexive(R3))  # 应返回 False
print("R3 反自反性:", isirreflexive(R3))  # 应返回 True

print("R4 自反性:", isreflexive(R4))  # 应返回 False
print("R4 反自反性:", isirreflexive(R4))  # 应返回 False
