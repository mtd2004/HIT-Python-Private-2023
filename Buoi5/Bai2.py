def largest_subset(input_set, target_sum):
    subset1 = set()
    subset2 = set()
    max_sum = 0

    for i in sorted(input_set):
        if max_sum + i <= max_sum:
            subset2.add(i)
            max_sum += i
        else:
            # Nếu thêm phần tử mới vượt quá mục tiêu, cập nhật tập hợp con lớn nhất
            if len(subset2) > len(subset1):
                subset1 = subset2.copy()
            # Loại bỏ các phần tử từ tập hợp con để giảm tổng đến khi có thể thêm phần tử mới
            while max_sum + i > target_sum and subset2:
                last_element = max(subset2)
                subset2.remove(last_element)
                max_sum -= last_element

            subset2.add(i)
            max_sum += i

    if len(subset2) > len(subset1):
        subset1 = subset2

    return subset1

n = int(input())
input_set = set(map(int, input().split()))
target_sum = int(input())

result_set = largest_subset(input_set, target_sum)

print(result_set)
