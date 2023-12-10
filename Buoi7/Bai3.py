class Matrix:
    def __init__(self, n, m, value):
        self.n = n
        self.m = m
        self.value = value

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Không thể cộng ma trận với kích thước khác nhau")
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.value[i][j] + other.value[i][j])
            result.append(row)
        return Matrix(self.n, self.m, result)

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Không thể trừ ma trận với kích thước khác nhau")
        result = []
        for i in range(self.n):
            row = []
            for j in range(self.m):
                row.append(self.value[i][j] - other.value[i][j])
            result.append(row)
        return Matrix(self.n, self.m, result)

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Không thể nhân ma trận vì không thỏa mãn điều kiện")
        result = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                element = 0
                for k in range(self.m):
                    element += self.value[i][k] * other.value[k][j]
                row.append(element)
            result.append(row)
        return Matrix(self.n, other.m, result)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row.append(self.value[i][j] / other)
                result.append(row)
            return Matrix(self.n, self.m, result)
        else:
            raise TypeError("Không thể thực hiện phép chia")

    def __eq__(self, other):
        if self.n != other.n or self.m != other.m:
            return False
        for i in range(self.n):
            for j in range(self.m):
                if self.value[i][j] != other.value[i][j]:
                    return False
        return True

    def __str__(self):
        matrix_str = ""
        for i in range(self.n):
            for j in range(self.m):
                matrix_str += str(self.value[i][j]) + " "
            matrix_str += "\n"
        return matrix_str.strip()

if __name__ == '__main__':
    # Tạo hai đối tượng Matrix và sử dụng các toán tử
    matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
    matrix2 = Matrix(2, 2, [[5, 6], [7, 8]])

    print("Ma trận 1:")
    print(matrix1)

    print("Ma trận 2:")
    print(matrix2)

    matrix_sum = matrix1 + matrix2
    print("Tổng hai ma trận :")
    print(matrix_sum)

    matrix_diff = matrix1 - matrix2
    print("Hiệu hai ma trận :")
    print(matrix_diff)

    matrix_product = matrix1 * matrix2
    print("Tích hai ma trận :")
    print(matrix_product)

    matrix_div = matrix1 / 2
    print("Thương hai ma trận : ")
    print(matrix_div)

    matrix_equal = matrix1 == matrix2
    print(matrix1 , ' = ' , matrix2 , matrix_equal , sep = '\n')