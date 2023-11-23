ban1 = set(input('Nhập Danh Sách Sinh Viên Đăng Ký Tại Bàn 1 : ').split())
ban2 = set(input('Nhập Danh Sách Sinh Viên Đăng Ký Tại Bàn 2 : ').split())

sinhvien2ban = ban1.intersection(ban2)
sinhvientonghop = ban1.union(ban2)
sinhvienchiban1 = ban1.difference(ban2)
sinhvienchiban2 = ban2.difference(ban1)
sinhvienchi1ban = ban1.symmetric_difference(ban2)

print("\nSinh viên đăng ký tại cả hai bàn:", sinhvien2ban)
print("\nDanh sách tổng hợp của các sinh viên đã đăng ký của cả hai bàn:", sinhvientonghop)
print("\nDanh sách sinh viên chỉ đăng ký tại bàn 1 mà không đăng ký tại bàn 2:", sinhvienchiban1)
print("\nDanh sách sinh viên chỉ đăng ký tại bàn 2 mà không đăng ký tại bàn 1:", sinhvienchiban2)
print("\nDanh sách sinh viên đăng ký ở duy nhất 1 bàn:", sinhvienchi1ban)