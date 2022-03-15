s=input().split()
n=int(s[0])
m=int(s[1])
for i in range(1, n, 2):
    print(str('.|.' * i).center(m, '-'))
for k in range((m-6)//2):
    print('-',end='' )
print('WELCOME',end='')
for k in range((m-6)//2):
    print('-',end='' )
print()
for i in range(n-2, -1, -2):
    print(str('.|.' * i).center(m, '-'))
