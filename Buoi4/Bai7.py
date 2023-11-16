def split_list(lst, n):
    length = len(lst)
    sub_length = length // n

    ans = []

    for i in range(n):
        start = i * sub_length
        end = start + sub_length
        sub_list = lst[start:end]
        ans.append(sub_list)

    return ans

a = ['a', 'b', 'c', 'd', 'e', 'f']
n = int(input())
ans = split_list(a, n)
print(ans)