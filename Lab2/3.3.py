def istransitive(X ,R):
    for(a , b) in R:
        for (c , d) in R:
             if b==c and (a,d) not in R:
                return False
    return True

X = {1, 2, 3, 4}

R1 = {(1, 2), (2, 3), (1, 3)}

R2 = {(1, 2), (2, 3), (3, 4)}

R3 = {(1, 2), (2, 3), (3, 2)}

print("R1 传递性:", istransitive(X, R1))
print("R2 传递性:", istransitive(X, R2))
print("R3 传递性:", istransitive(X, R3))