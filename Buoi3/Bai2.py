n = int(input())
m = int(input())
for i in range(0, n, 1):
    s = input()
    ans = len(s)
    for j in range(0 , ans - m , 1) :
        print(s[j] , sep='' , end='')
    for j in range(ans - 1 , ans - m - 1 , -1):
        print(s[j], sep='', end='')
    print()
