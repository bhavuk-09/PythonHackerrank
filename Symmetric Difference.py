# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
ms=map(int,input().split())
lm=set(ms)

n=int(input())
ns=map(int,input().split())
ln=set(ns)

res=lm.symmetric_difference(ln)
# res=list(map(int,res))
# res.sort()
res=list(res)
res.sort()

for i in range(len(res)):
    print(res[i])
