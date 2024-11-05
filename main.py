# a = ["1", "3", "3", 8, "2", "5", 781, "9", "2", "3", 1]
#
# cur_num = ""
# result = []
# length = len(a) - 1
#
# for index, num in enumerate(a):
#     if type(num) is str:
#         cur_num += num
#     else:
#         result.extend([int(cur_num), num])
#         cur_num = ""
#
#     if index == length and type(num) is str:
#         result.append(int(cur_num))
#
# print(max(result))

a = ["1", "3", "3", 8, "2", "5", 781, "9", "2", "3"]

# cur_num = ""
# result = []
# length = len(a)
#
# for index in range(length):
#     num = a[index]
#
#     if type(num) is str:
#         cur_num += num
#     else:
#         result.extend([int(cur_num), num])
#         cur_num = ""
#
#     if index == length - 1 and type(num) is str:
#         result.append(int(cur_num))
#
#
# print(max(result))


a = ["1", "3", "3", 8, "2", "5", 781, "9", "2", "3"]

print(a[::-1][2:5])


# cur_num = ""
# max_number = 0
#
#
# for num in a:
#     if type(num) is str:
#         cur_num += num
#     else:
#         if int(cur_num) > max_number and int(cur_num) > num:
#             max_number = int(cur_num)
#         else:
#             if num > max_number:
#                 max_number = num
#         cur_num = ""
# else:
#     if cur_num:
#         if int(cur_num) > max_number:
#             max_number = int(cur_num)
#
# print(max_number)