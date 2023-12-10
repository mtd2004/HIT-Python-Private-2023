class Pycon:
    count = 0

    def __init__(self , name , age):
        Pycon.count += 1
        self.id = Pycon.count
        self.name = name
        self.age = age

    def __str__(self):
        return f"Id: {self.id} || Tên: {self.name} || Tuổi: {self.age}"

    @classmethod
    def averAge(cls, pycons):
        total_age = sum(pycon.age for pycon in pycons)
        return total_age / len(pycons)

    @classmethod
    def nhap(cls):
        name = input()
        age = int(input())
        pycon = Pycon(name, age)
        return pycon

if __name__ == '__main__':
    n = int(input())
    pycons = []

    for i in range(n):
        pycon = Pycon.nhap()
        pycons.append(pycon)

    # In thông tin của các Pycon
    for pycon in pycons:
        print(pycon)
    #Tính và in độ tuổi trung bình
    avg_age = Pycon.averAge(pycons)
    print(f"Trung bình tuổi: {avg_age}")