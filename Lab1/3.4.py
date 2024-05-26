import random

def createset(m, n):
    return set(random.sample(range(m), n))


A = createset(10, 4)
B = createset(15, 12)
C = createset(12, 6)

Set1 = (A | B) | C
Set2 = A | (B | C)
Set3 = (A & B) & C
Set4 = A & (B & C)
print("(A∪B)∪C=", Set1)
print("A∪(B∪C)", Set2)
print("A∩(B∩C)", Set3)
print("A∩(B∩C)", Set4)
