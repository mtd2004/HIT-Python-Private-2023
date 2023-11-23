input_str = input()

frequency = {}

for char in input_str:
    # method get: kiểm tra xem ký tự đã có trong dictionary chưa
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
