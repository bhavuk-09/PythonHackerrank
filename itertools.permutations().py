# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s=input().split()
s1=s[0]
k=int(s[1])

res=list(permutations(s1,k))
r1=[]
for i in range(len(res)):
    st=''
    st+= res[i][0]+ res[i][1]
    r1.append(st)
    
r1.sort()
for i in range(len(r1)):
    print(r1[i])
    
