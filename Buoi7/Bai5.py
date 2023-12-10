class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    @staticmethod
    def chuyen_hon_so(phan_so):
        phan_nguyen = phan_so.tu_so // phan_so.mau_so
        tu_so = phan_so.tu_so % phan_so.mau_so
        mau_so = phan_so.mau_so
        return HonSo(phan_nguyen, tu_so, mau_so)

    def rut_gon(self):
        ucln = self.tim_ucln(self.tu_so, self.mau_so)
        tu_so_rut_gon = self.tu_so // ucln
        mau_so_rut_gon = self.mau_so // ucln
        return PhanSo(tu_so_rut_gon, mau_so_rut_gon)

    @staticmethod
    def tim_ucln(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"


class HonSo:
    def __init__(self, phan_nguyen, tu_so, mau_so):
        self.phan_nguyen = phan_nguyen
        self.tu_so = tu_so
        self.mau_so = mau_so

    @staticmethod
    def chuyen_phan_so(hon_so):
        tu_so = hon_so.phan_nguyen * hon_so.mau_so + hon_so.tu_so
        mau_so = hon_so.mau_so
        return PhanSo(tu_so, mau_so)

    def __str__(self):
        return f"{self.phan_nguyen} {self.tu_so}/{self.mau_so}"


class Math(PhanSo, HonSo):
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        if isinstance(other, Math):
            a = self.a.rut_gon()
            b = other.a.rut_gon()
            tu_so = a.tu_so * b.mau_so + b.tu_so * a.mau_so
            mau_so = a.mau_so * b.mau_so
            return Math(PhanSo(tu_so, mau_so).rut_gon())
        else:
            raise TypeError("Unsupported operand type for addition.")

    def __mul__(self, other):
        if isinstance(other, Math):
            a = self.a.rut_gon()
            b = other.a.rut_gon()
            tu_so = a.tu_so * b.tu_so
            mau_so = a.mau_so * b.mau_so
            return Math(PhanSo(tu_so, mau_so).rut_gon())
        else:
            raise TypeError("Unsupported operand type for multiplication.")

    def __str__(self):
        return str(self.a)

if __name__ == '__main__':
    # Tạo đối tượng Math với phân số và hỗn số
    phan_so = PhanSo(3, 4)
    hon_so = HonSo(2, 1, 3)

    # Chuyển phân số thành hỗn số và in lại
    hon_so_chuyen = HonSo.chuyen_phan_so(phan_so)
    print("Hỗn số chuyển từ phân số:")
    print(hon_so_chuyen)

    # Chuyển hỗn số thành phân số và in lại
    phan_so_chuyen = PhanSo.chuyen_hon_so(hon_so)
    print("Phân số chuyển từ hỗn số:")
    print(phan_so_chuyen)

    # Tạo đối tượng Math và sử dụng các phép toán
    math1 = Math(phan_so)
    math2 = Math(hon_so)

    print("a:", math1)
    print("b:", math2)

    result1 = math1 + math2
    print("a + b:", result1)

    result2 = math2 + math1
    print("b + a:", result2)

    result3 = math1 * math2
    print("a * b:", result3)

    result4 = math2 * math1
    print("b * a:", result4)