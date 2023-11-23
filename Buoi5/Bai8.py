championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Tryndamere"]
dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}
]

champion_dict = {champion: data for champion, data in zip(championLOL, dataLOL)}

champion_name = input("Nhập tên champion: ")

if champion_name in champion_dict:
    price = champion_dict[champion_name]["price"]
    print(f"Gia cua {champion_name} la: {price}")
else:
    print(f"Champion {champion_name} khong ton tai trong cua hang.")
