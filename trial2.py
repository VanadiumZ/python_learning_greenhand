# def abstract_value(a):
#     if isinstance(a, (int, float)):
#         return abs(a)
    
#     try:
#         b = float(a)
#         return abs(b)
#     except:
#         return None
    
# print(abstract_value(10))
# print(abstract_value("-1.5"))
# print(abstract_value((3, 2)))
# print(abstract_value("a"))

# def list_median(input_list):
#     n = len(input_list)
#     input_list.sort()
#     if n == 0:
#         return None
#     elif n % 2 == 0:
#         mid = (input_list[(n//2)-1] + input_list[n//2]) / 2
#         return mid
#     elif n % 2 != 0:
#         return input_list[n//2]
    
# print(list_median([3, 2, 5]))
# print(list_median([2, 5, 3, 4]))
# print(list_median([]))

def count_sum_int_float(input_list):
    count = 0
    value = 0
    for item in input_list:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            count += 1
            value += float(item)
        else:
            continue

    if len(input_list) == 0 or count == 0:
        return (0, None)
    
    return (count, value)
    
print(count_sum_int_float([2, "f", 5, 'a', 'b', True, False]))
print(count_sum_int_float(["a", "b"]))
print(count_sum_int_float([(1, 2), 1, 2, [1, 2]]))

# def sum_int_list(input_list, target):
#     # input_list is a list of integer
#     # target is an interger
#     output_list = []
#     for i in input_list:
#         for j in input_list:
#             if i + j == target and input_list.index(i) < input_list.index(j):
#                 output_list.append((input_list.index(i), input_list.index(j)))
#     output_list.sort()
#     return output_list
# print(sum_int_list([2, 7, 11, 15], 9))
# print(sum_int_list([-3, 3, -4, -8, 7], -1))
# print(sum_int_list([-3, 3, -4, -8, 7], 1))


