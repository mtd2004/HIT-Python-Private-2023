# Tạo ma trận a và ma trận nghịch đảo a_t
def create_matrix(a : list , n : int , m : int) -> None:
    """
    Hàm create_matrix thực hiện tạo 1 ma trận sau đó in ra
    ma trận nghịch đảo của ma trận đó
    :param a: list
    :param n: số hàng
    :param m: số cột
    :return: Không trả về giá trị gì (None)
    """
    for i in range(n):
        a[i] = list(map(int, input().split()))
    a_t = [[row[i] for row in a] for i in range(len(a))]
    for i in range(n):
        for j in range(m):
            print(a_t[i][j], end=' ')
        print()

# Hàm main
if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    create_matrix(a , n , m)
