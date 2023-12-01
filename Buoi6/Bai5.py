# Hàm tính ước chung lớn nhất
def gcd(a : int, b : int) -> int:
    """
    Hàm gcd(a, b) thực hiện tìm ước chung lớn nhất của hai số a và b
    :param a: int
    :param b: int
    :return: ước chung lớn nhất của hai số a và b : int
    """
    while(b != 0):
       a , b = b , a % b
    return a

# Hàm tính tích n phân số
def xu_ly() -> None:
    """
    Hàm xu_ly() thực hiện việc tính tích n phân số sau đó in ra
    dưới dạng tối giản
    :return: tử số : int và mẫu số : int
    """
    n = int(input())
    res1 , res2 = 1 , 1
    for i in range(n):
        a , b = map(int , input().split())
        res1 *= a
        res2 *= b
    ans = gcd(res1 , res2)
    print(res1 // ans , res2 // ans)

# Hàm main
if __name__ == '__main__':
    xu_ly()
