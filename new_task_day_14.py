# 1. Find the two max and two min from the list.

# num =  [2, 2, 56, 78, 89, 90, 43, 101, 201, 202, 202, 203]

# new_num_list = []
# smallest_no = 0
# final_order = []
# loop_runs = True

# for i in range(0, len(num)):
#     for j in range(i, len(num)):
#         if num[j] != num[i-1] and num[i] not in new_num_list:
#             new_num_list.append(num[i])

# while loop_runs:
#     for i in new_num_list:
#         if i == smallest_no and i not in final_order:
#             final_order.append(i)
#     smallest_no+=1
#     if len(final_order) == len(new_num_list):
#         loop_runs = False

# print(final_order)

# print(f"Minimum Numbers are : ({final_order[0]}, {final_order[1]}) ")
# print(f"Maximum Numbers are : ({final_order[-2]}, {final_order[-1]}) ")


# ------------------------------------------------------------------------------------------------


# 2. Write a program to replace the vowels by * from a string.

# string = "visiontrek communications"
# vowels = "aeiou"
# char_list = []

# for char in string:
#     char_list.append(char)

# for i in range(0, len(char_list)):
#     if char_list[i] in vowels:
#         char_list[i] = '*'
    
# print(''.join(char_list))


# ------------------------------------------------------------------------------------------------


# 3. Write a program to write even values and odd value strings from a list.

# list = ["abc", "cdzf", "xyza"]
# even = []
# odd = []

# for item in list:
#     if len(item)%2==0:
#         even.append(item)
#     else:
#         odd.append(item)

# print(f"Even : {even}")
# print(f"Odd : {odd}")


# ------------------------------------------------------------------------------------------------


# 4. Write a program to add two lists into a dictionary.

# list = ['key', 'key2', 'key3']
# list2 = [1, 'abc', 3.0]

# dict1 = {}

# for i in range(0, len(list)):
#     dict1[list[i]] = list2[i]

# print(dict1)


# ------------------------------------------------------------------------------------------------


# 5. Write a program to reverse a string or number.

# Method #1

# text = str(input("Enter the string : "))

# # text = '12345'
# text_list = []
# reversed = []
# i = len(text)-1

# for j in range(0, len(text)):
#     reversed.append(text[i])
#     i-=1

# print(''.join(reversed))


# ------------------------------------------------------------------------------------------------


# 6. Write a program to give input eg for 7 -> 7, 17, 37, 67, 107, 157

# num = int(input("Enter a number : "))
# add = 0
# for i in range(0, num):
#     num+=add
#     add+=10
#     print(num)


# ------------------------------------------------------------------------------------------------


# # 7. Write a program to print an output.

# list = ["string", "vision"....]
# output = ["s","t","r","i","n","g"....]

# list = ["string", "vision", "trek", "communications"]

# output = []
# for word in list:
#     for char in word:
#         output.append(char)

# print(output)
    

# ------------------------------------------------------------------------------------------------