# Enter your code here. Read input from STDIN. Print output to STDOUT
e=int(input())
E=map(int,input().split())
f=int(input())
F=map(int,input().split())
E=set(E)
F=set(F)
D= E.difference(F)
D=list(D)
print(len(D))Set
