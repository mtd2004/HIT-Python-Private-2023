def xu_ly(a):
    ans = []
    for i in a:
        if isinstance(i, list):
            ans.extend(xu_ly(i))
        else:
            ans.append(i)
    return ans

a= [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
ans = xu_ly(a)

print(ans)