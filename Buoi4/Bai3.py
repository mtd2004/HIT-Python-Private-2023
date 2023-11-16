import re

def tinh_tong(str):
    so = re.findall(r'-?\d+', str)  
    tong = sum(map(int, so))  
    return tong

str = input()
ans = tinh_tong(str)
print(ans)