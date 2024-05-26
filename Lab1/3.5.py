A = {1, 2, 4, 5, 8, 9}
B = {2, 3, 6, 7, 8, 10}
def compare(A,B):
    if A == B: print(A, "=",B)
    if A != B: print(A, "≠",B)
    if A <= B: print(A, "⊆",B)
    if A < B: print(A, "⊂",B)
    if A >= B: print(A, "⊇",B)
    if A > B: print(A, "⊃",B)

compare(A&B, A)
compare(A|B,A)

