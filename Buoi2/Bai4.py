a = int(input("Nhập số a: "))

# Trả về số lượng các bits cần thiết để biểu diễn số a ở dạng nhị phân
print("Số bits cần thiết để biểu diễn a:", a.bit_length())

# Kiểm tra danh sách các thuộc tính và phương thức hiện tại của một biến có kiểu dữ liệu là number
a = 100
b = 4.5
c = 4 + 5j
print(dir(a) , dir(b) , dir(c) , sep = "\n")