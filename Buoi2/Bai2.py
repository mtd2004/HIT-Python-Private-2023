# Nhập chuỗi ký tự
str = input("Nhập chuỗi ký tự: ")

# Kiểm tra có chữ "hit" hoặc "HIT" trong chuỗi
if "hit" in str or "HIT" in str:
    print("True")
else:
    print("False")

# Kiểm tra không có số 14 trong chuỗi
if "14" not in str:
    print("True")
else:
    print("False")