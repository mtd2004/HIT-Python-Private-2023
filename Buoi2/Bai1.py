# Cho 2 số a, b
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

# a cộng b
print("a + b =", a + b)

# a trừ b
print("a - b =", a - b)

# a nhân b
print("a * b =", a * b)

# a chia lấy nguyên b
print("a // b =", a // b)

# a mũ b
print("a ^ b =", a ** b)

# a chia dư b
print("a % b =", a % b)

# so sánh a và b
if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")

# a AND b
print("a AND b =", a & b)

# a OR b
print("a OR b =", a | b)

# a XOR b
print("a XOR b =", a ^ b)

# NOT a == b
print("NOT a == b =", not (a == b))

# a dịch phải 5 bit
print("a dịch phải 5 bit =", a >> 5)

# a dịch trái 6 bit
print("a dịch trái 6 bit =", a << 6)

# in hệ cơ số 2 đảo ngược của a
print("Hệ cơ số 2 đảo ngược của a:", bin(a)[::-1])