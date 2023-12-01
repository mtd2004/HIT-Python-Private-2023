import math

def doc_file(filename : str) -> tuple:
    """
    Hàm doc_file thực hiện đọc dữ liệu từ 1 file và lấy ra tọa
    độ hai điểm A và B
    :param filename: tên file cần đọc : string
    :return: Hai điểm A và B : tuple
    """
    with open(filename , 'r') as file:
        data = file.read().split()
    diem_A = (float(data[1]) , float(data[2]))
    diem_B = (float(data[4]), float(data[5]))
    return diem_A , diem_B

def khoang_cach(diem_A : tuple, diem_B : tuple) -> float:
    """
    Hàm khoang_cach thực hiện tính khoảng cách giữa 2 điểm A và B
    :param diem_A: tuple
    :param diem_B: tuple
    :return: khoảng cách giữa 2 điểm A và B : float
    """
    res = math.sqrt((diem_B[0] - diem_A[0]) ** 2 + (diem_B[1] - diem_A[1]) ** 2)
    res = round(res , 2)
    return res

def ghi_file(filename : str , diem_A : tuple , diem_B : tuple, res : float) -> None:
    """
    Hàm ghi file thực hiện ghi kết quả vào file theo định dạng yêu cầu
    :param filename: str
    :param diem_A: tuple
    :param diem_B: tuple
    :param res: float
    :return: None
    """
    with open(filename , 'w') as file:
        file.write(f"A({diem_A[0]}, {diem_A[1]}) B({diem_B[0]}, {diem_B[1]}) AB = {res}")

if __name__ == '__main__':
    input_filename = "input.txt"
    output_filename = "output.txt"
    diem_A , diem_B = doc_file(input_filename)
    res = khoang_cach(diem_A , diem_B)
    ghi_file(output_filename , diem_A , diem_B , res)