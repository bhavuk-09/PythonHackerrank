# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    n=int(input())
    N=input().split()
    n1=int(input())
    N1=input().split()
    N=set(N)
    N1=set(N1)
    R= N1.intersection(N)== N
    # R=False
    print(R)
