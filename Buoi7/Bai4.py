class Hiter:
    danh_sach_hiter = []

    def __init__(self, _id, ten, tuoi, gen):
        self.id = _id
        self.ten = ten
        self.tuoi = tuoi
        self.gen = gen
        Hiter.danh_sach_hiter.append(self)

    def __str__(self):
        return f"ID: {self.id}, Tên: {self.ten}, Tuổi: {self.tuoi}, Giới tính: {self.gen}"

    @staticmethod
    def nhap():
        _id = input("Nhập ID: ")
        ten = input("Nhập Tên: ")
        tuoi = input("Nhập Tuổi: ")
        gen = input("Nhập Giới tính: ")
        return Hiter(_id, ten, tuoi, gen)

    @staticmethod
    def danh_sach():
        for hiter in Hiter.danh_sach_hiter:
            print(hiter)


class Ban:
    def __init__(self, id_ban, ten_ban, truong_ban):
        self.id_ban = id_ban
        self.ten_ban = ten_ban
        self.truong_ban = truong_ban
        self.thanh_vien = []

    def __str__(self):
        return f"ID Bàn: {self.id_ban}, Tên Bàn: {self.ten_ban}, Trưởng Ban: {self.truong_ban.ten}"

    def dsHiter(self):
        for hiter in self.thanh_vien:
            print(hiter)

    def xoa(self):
        ten_hiter_xoa = input("Nhập tên Hiter cần xóa: ")
        for hiter in self.thanh_vien:
            if hiter.ten == ten_hiter_xoa:
                self.thanh_vien.remove(hiter)
                print(f"Hiter {ten_hiter_xoa} đã được xóa khỏi ban {self.ten_ban}")
                return
        print(f"Hiter {ten_hiter_xoa} không tồn tại trong ban {self.ten_ban}")

    def add(self, hiter):
        if hiter not in self.thanh_vien and hiter in Hiter.danh_sach_hiter:
            self.thanh_vien.append(hiter)
            print(f"Hiter {hiter.ten} đã được thêm vào ban {self.ten_ban}")
        elif hiter in self.thanh_vien:
            print(f"Hiter {hiter.ten} đã có trong ban {self.ten_ban}")
        else:
            print(f"Hiter {hiter.ten} không có trong danh sách Hiter")



n = int(input("Nhập số lượng Hiter: "))
danh_sach_hiter = []
for i in range(n):
    print(f"Nhập thông tin Hiter thứ {i + 1}:")
    hiter = Hiter.nhap()
    danh_sach_hiter.append(hiter)


print("Thông tin các Hiter:")
for hiter in danh_sach_hiter:
    print(hiter)


m = int(input("Nhập số lượng Ban: "))
danh_sach_ban = []
for i in range(m):
    print(f"Nhập thông tin Ban thứ {i + 1}:")
    id_ban = input("Nhập ID Bàn: ")
    ten_ban = input("Nhập Tên Bàn: ")
    print("Chọn Trưởng Ban từ danh sách Hiter:")
    Hiter.danh_sach()
    truong_ban_id = input("Nhập ID của Trưởng Ban: ")
    truong_ban = next((hiter for hiter in danh_sach_hiter if hiter.id == truong_ban_id), None)
    if truong_ban:
        ban = Ban(id_ban, ten_ban, truong_ban)
        danh_sach_ban.append(ban)
    else:
        print("ID Trưởng Ban không hợp lệ, vui lòng nhập lại thông tin Ban.")


print("Thông tin các Ban:")
for ban in danh_sach_ban:
    print(ban)


ten_ban_can_xoa = input("Nhập Tên Bàn cần xóa Hiter: ")
for ban in danh_sach_ban:
    if ban.ten_ban == ten_ban_can_xoa:
        ban.xoa()
        break
else:
    print(f"Bàn {ten_ban_can_xoa} không tồn tại trong danh sách Ban")


ten_ban_can_them = input("Nhập Tên Bàn cần thêm Hiter: ")
for ban in danh_sach_ban:
    if ban.ten_ban == ten_ban_can_them:
        print("Chọn Hiter từ danh sách:")
        Hiter.danh_sach()
        hiter_them_id = input("Nhập ID của Hiter cần thêm: ")
        hiter_them = next((hiter for hiter in danh_sach_hiter if hiter.id == hiter_them_id), None)
        if hiter_them:
            ban.add(hiter_them)
        else:
            print("ID Hiter không hợp lệ, vui lòng chọn lại.")
        break
else:
    print(f"Bàn {ten_ban_can_them} không tồn tại trong danh sách Ban")