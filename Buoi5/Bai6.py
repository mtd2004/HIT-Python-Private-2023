diem_tong_ket = {
    "SV001": 1.5,
    "SV002": 2.0,
    "SV003": 3.2,
    "SV004": 2.0,
    "SV005": 2.5,
    "SV006": 2.8,
    "SV007": 3.6,
    "SV008": 2.7,
    "SV009": 3.5,
    "SV010": 2.9,
}

so_sinh_vien= sum(2.5 <= diem <= 3.5 for diem in diem_tong_ket.values())
print(f"Số sinh viên có điểm tổng kết trong đoạn [2.5, 3.5]: {so_sinh_vien}")

ma_sinh_vien_moi = "SV011"
diem_moi = 3.7
diem_tong_ket[ma_sinh_vien_moi] = diem_moi

sinh_vien_can_xoa = [ma_sinh_vien for ma_sinh_vien, diem in diem_tong_ket.items() if diem < 2.0]
for ma_sinh_vien in sinh_vien_can_xoa:
    del diem_tong_ket[ma_sinh_vien]

print("Từ điển sau khi thực hiện các thao tác:")
for ma_sinh_vien, diem in diem_tong_ket.items():
    print(f"{ma_sinh_vien}: {diem}")
