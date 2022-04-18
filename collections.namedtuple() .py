# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
s= input().split()
for j in range(len(s)):
    if s[j]=='MARKS':
        ind=j
        break
sum=0    
for i in range(t):
    f=input().split()
    sum+=int(f[ind])
res= sum/t
print(res)
    
