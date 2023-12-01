# Hàm tính tích các tham số truyền vào
def MyMultiple(*args) -> float:
    """
    Hàm MyMultiple thực hiện tính tích của các tham số truyền vào
    :param args: Các tham số truyền vào
    :return: tích của các tham số truyền vào
    """
    res = 1
    for i in args:
        res *= i
    return float(res)

# Hàm main
if __name__ == '__main__':
    print(MyMultiple(1 , 2 , 3 , 4))
    print(MyMultiple(5 , 5 , 5))
    print(MyMultiple(1.2 , 5))