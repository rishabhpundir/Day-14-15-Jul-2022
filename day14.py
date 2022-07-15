# tup = (1, 3, 6, 2, 9, 0, 0, 7, 4)
# # new_tup = tuple(sorted(tup))
# new_set = set(tup)
# new_set2 = set((5, 1, 4, 6, 6, 4))
# print(type(new_set2))
# print(new_set2)
# new_list = set(new_set2)
# # print(type(new_tup))
# # print(new_tup)
# print(new_set)
# print(new_list)


# -----------------------------------------------------------------------------------

# lang = ['java', 'python', '.NET', 'PHP', 'java', 'python']

# #------------Remove duplicates-------------------

# Method #1

# new_list = []
# for i in range(0, len(lang)):
    
#     for j in range(i+1, len(lang)):
#         if lang[j] != lang[i] and lang[j] not in new_list:
#             new_list.append(lang[j])

# print(new_list)


# # ----------- OR ----------


# Method #2

# temp = list(set((lang)))
# print(temp)

# #---------------Count repetition---------------------

# lang_dict = {}
# for i in range(0, len(lang)):
#     counter = 1
#     for j in range(i, len(lang)):
#         if lang[i] == lang[j] and lang[j] in lang_dict:
#             counter+=1
#     lang_dict[lang[i]] = counter

# print(lang_dict)


# -----------------------------------------------------------------------------------

# num = [1, 2, 7, 4, 6, 3, 8, 3, 7, 3, 8, 3, 7, 2, 1, 1, 200]

# #------------Remove duplicates & Ordered in Ascension-------------------

# new_num_list = []
# smallest_no = 0
# final_order = []
# loop_runs = True

# for i in range(0, len(num)):
#     for j in range(i+1, len(num)):
#         if num[j] != num[i] and num[j] not in new_num_list:
#             new_num_list.append(num[j])

# print(new_num_list)

# while loop_runs:
#     for i in new_num_list:
#         if i == smallest_no and i not in final_order:
#             final_order.append(i)
#     smallest_no+=1
#     if len(final_order) == len(new_num_list):
#         loop_runs = False

# print(final_order)


# # #---------------Count repetition & Ordered in Ascension---------------------

# num_dict = {}
# smallest_no = 0
# final_ordered_dict = {}
# loop_runs = True

# for i in range(0, len(num)):
#     counter = 1
#     for j in range(i, len(num)):
#         if num[i] == num[j] and num[j] in num_dict:
#             counter+=1
#     num_dict[num[i]] = counter

# # print(num_dict)

# while loop_runs:
#     for i in num_dict:
#         if i == smallest_no and i not in final_ordered_dict:
#             final_ordered_dict[i] = num_dict[i]
#     smallest_no+=1
#     if len(final_ordered_dict) == len(num_dict):
#         loop_runs = False

# print(final_ordered_dict)


# -----------------------------------------------------------------------------------