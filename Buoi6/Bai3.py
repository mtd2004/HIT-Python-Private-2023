# Hàm để nhập mảng
def nhap_mang() -> None:
    """
    Hàm nhap_mang() thực hiện nhập một mảng n phần tử từ bàn phím
    :return: Giá trị cả về là 1 list
    """
    n = int(input())
    a = []
    a = list(map(int , input().split()))
    return a

# Hàm để tính tổng các số từ vị trí đầu đến vị trí x
def tinh_tong(a : list, x : int) -> int:
    """
    Hàm tinh_tong(a , x) thực hiện việc tính tổng của các số
    có vị trí từ đầu đến vị trí x trong list a
    :param a: list
    :param x: int
    :return: tổng các số có vị trí từ đầu đến vị trí x trong list a : int
    """
    res = 0
    for i in range(x + 1):
        res += a[i]
    return res

# Hàm main
if __name__ == '__main__':
    a = nhap_mang()
    testcase = int(input())
    for i in range(testcase):
        x = int(input())
        print(tinh_tong(a , x))