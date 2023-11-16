def check(n):
    if n % 10 == 1 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9:
        return True
    return False

n = int(input())
a = []
a = list(map(int , input().split()))

ans = []
count = 0
se = set()
for i in range(n):
    if check(a[i]):
        count += 1
        ans.append(a[i])
ans.sort() 
print(count)
for i in ans:
    print(i, end=" ")