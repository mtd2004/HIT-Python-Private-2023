import math

a1 , b1 , a2 , b2 , a3 , b3 = map(float , input().split())
ans1 = math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)
ans2 = math.sqrt((a1 - a3) ** 2 + (b1 - b3) ** 2)
ans3 = math.sqrt((a2 - a3) ** 2 + (b2 - b3) ** 2)
if (ans1 + ans2) > ans3 and (ans1 + ans3) > ans2 and (ans2 + ans3) > ans1 :
    print('TAM GIÁC')
else :
    print('KHÔNG PHẢI TAM GIÁC')

