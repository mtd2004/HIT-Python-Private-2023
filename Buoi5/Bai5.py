input_set = set(map(int, input("Nhập dãy số : ").split()))

if 11 not in input_set:
    input_set.add(11)
    print("Đã thêm số 11 vào set.")

print("Set sau khi kiểm tra : ")
print(input_set)

lucky_number = 11
number_pairs = {(num, lucky_number - num) for num in input_set if lucky_number - num in input_set}

result_tuple = tuple(number_pairs)
total_sum = sum(map(sum, result_tuple))

print(f"Các cặp số có tổng bằng {lucky_number}: {result_tuple}")
print(f"Tổng của các cặp số: {total_sum}")
