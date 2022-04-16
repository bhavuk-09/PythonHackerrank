# Enter your code here. Read input from STDIN. Print output to STDOUT
e=int(input())
E=map(int,input().split())
E=set(E)

f=int(input())
F=map(int,input().split())
F=set(F)

R=E.intersection(F)
R=list(R)
print(len(R))
