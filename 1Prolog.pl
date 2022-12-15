student(a,man,3).
student(b,woman,4).
student(c,man,3).
student(d,woman,5).
molodec(X,Y):-student(X,Y,Z),Z=4.
molodec(X,Y):-student(X,Y,Z),Z=5.



?-molodec(X,woman)