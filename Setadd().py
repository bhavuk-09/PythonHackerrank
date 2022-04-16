# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
# N=set(input().split())
# N=list(N)
# print(len(N))
l=[]
for i in range(0,n):
    temp=input()
    l.append(temp)
l=set(l)
l=list(l)
print(len(l))
