# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
a=map(int,input().split())
b=map(int,input().split())
c=list(product(a,b))
for i in range(len(c)):
    print(c[i], end=' ')
