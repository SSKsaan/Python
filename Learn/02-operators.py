n1 = 3; n2 = 11 # to separate statements in same line ; can still be used

# basic addition(+) & subtraction(-):
print(n1,'+',n2,'=', n1+n2 ,';',n1,'-',n2,'=', n1-n2)
# multiplication (*) & power (**):
print(n1,'x',n2,'=', n1*n2 ,';',n1,'^ 2 =', n1**2)
# Full division result (/) & Integer Division result (//):
print(n2,'/',n1,'=', n2/n1 ,'or', n2//n1)
# Remainder of division (%):
n2 %= n1; print('& Remainder =', n2)
# [var = var op val] => [var op= val] (shorthand)
# increment(++) & decrement(--) aren't available in python as operators
print(n1, '=', n2, 'is', n1==n2)
print(n1, 'is not', n2, ':', n1!=n2)
