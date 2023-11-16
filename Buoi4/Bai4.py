n = int(input())
a = []
a = list(map(int , input().split()))
chan , le = 0 , 0

for i in a:
    if i % 2 == 0:
        chan += i
    else:
        le += i

if chan > le:
    print('even')
elif chan == le:
    print('equal')
else:
    print('odd')