def truthtable3(s):
    print("P  Q  R ",s)
    for i in range (2):
        for j in range (2):
            for k in range (2):
                [P,Q,R]=[i,j,k]
                print(i," ",j," ",k," ",bool(eval(s)))

s1='(not(not(Q&R)))|((not Q)|(not R))'
s2='not P or (not Q or R)'
truthtable3(s1)
truthtable3(s2)