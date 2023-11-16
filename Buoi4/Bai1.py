from datetime import datetime

def count_days(str):
    date = datetime.strptime(str, "%d/%m/%Y")

    end_of_year = datetime(date.year, 12, 31)

    remaining_days = (end_of_year - date).days
    
    return remaining_days

while True:
    str = input()
    d, m , y = list(map(int, str.split('/')))
    if 1 <= d <= 31 and 1 <= m <= 12 and y >= 1000:
        break
    else:
        print("Invalid")
days= count_days(str) + 1
print( days)