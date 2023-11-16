def group_values(lst):
    grouped_list = []
    sub_list = []

    for item in lst:
        if not sub_list or item == sub_list[0]:
            sub_list.append(item)
        else:
            grouped_list.append(sub_list)
            sub_list = [item]

    if sub_list:
        grouped_list.append(sub_list)

    return grouped_list

lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
grouped_list = group_values(lst)
print(grouped_list)