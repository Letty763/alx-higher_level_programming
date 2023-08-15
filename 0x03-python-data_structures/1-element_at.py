def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

my_list = [1, 2, 3, 4, 5]
idx = 3
result = element_at(my_list, idx)
if result is not None:
    print("Element at index {} is {}".format(idx, result))
else:
    print("Index out of range or negative.")

