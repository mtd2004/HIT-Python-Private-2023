n = int(input())
for i in range(0 , n , 1) :
    s = input()
    x = int(input())
    y = int(input())
    ans = x + y
    print(i + 1 , s , ans , end = ' ')
    if ans >= 190 :
        print('Xuất sắc')
    elif ans >= 150 and ans < 190 :
        print('Giỏi')
    elif ans >= 100 and ans < 150 :
        print('Khá')
    else :
        print('Yếu')

