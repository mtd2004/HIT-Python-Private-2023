import random

def generate_username(student_id):
    return "2021" + str(student_id).zfill(6)

def generate_password(major, student_id):
    return random.choice(["CNTT", "KHMT", "KTPM", "HTTT"]) + str(student_id)

def create_accounts(n):
    accounts = {}
    for i in range(n):
        account_number = i + 1
        username = generate_username(1600000 + account_number)
        password = generate_password(username[:4], username[4:])
        account_info = {
            "Username": username,
            "Password": password
        }
        accounts["Account" + str(account_number)] = account_info

    return accounts

N = int(input("Nhập số lượng tài khoản sinh viên (10 <= N < 100000): "))

student_accounts = create_accounts(N)

for account_name, account_info in student_accounts.items():
    print(f"{account_name} : {account_info}")
