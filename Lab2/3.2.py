def issymmetric(X,R):
    flag=True
    for (a,b) in R:
        if (b,a) not in R: flag= False
        else :continue
    return flag

def isantisymmetric(X,R):
    for (a,b) in R:
        if a!= b and (b,a) in R: return False
    return True

X = {1, 2, 3, 4}

# 对称关系
R1 = {(1, 2), (2, 1), (2, 3), (3, 2), (3, 4), (4, 3)}


# 反对称关系
R3 = {(1, 1), (2, 2), (3, 3), (1, 2), (3, 4)}


# 测试结果
print("R1 对称性:", issymmetric(X, R1))  # 应返回 True
print("R1 反对称性:", isantisymmetric(X, R1))  # 应返回 False


print("R3 对称性:", issymmetric(X, R3))  # 应返回 False
print("R3 反对称性:", isantisymmetric(X, R3))  # 应返回 True

