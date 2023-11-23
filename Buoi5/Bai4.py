n = int(input("Nhập số lượng phần tử của mảng a: "))

a = []
for i in range(n):
    a.append(input(f"Nhập phần tử thứ {i + 1} của mảng a: "))

# Tạo tuple b từ mảng a
b = tuple(a)

# In tuple b ra màn hình
print("Tuple b được tạo từ mảng a:")
print(b)

# Đếm số phần tử trong b có dạng số
so_dang_so = sum(str(element).isdigit() for element in b)
print(f"Số phần tử trong b có dạng số là: {so_dang_so}")
