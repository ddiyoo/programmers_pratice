element = 2
some_list= [1, 2, 3, 5, 8, 13, 21, 34, 55]

# num_list = []
# print(some_list[len(some_list)//2])
# while element != some_list[len(some_list)//2]:
#
#     if element < some_list[len(some_list)//2]:
#         some_list = some_list[:(len(some_list)//2)+1]
#
#     elif element > some_list[len(some_list)//2]:
#         some_list = some_list[(len(some_list)//2):]
# print(num_list)

#
# len_list = []
# while element!=some_list[len(some_list)//2]:
#     # print('len:',len(some_list)//2)
#
#     if element < some_list[len(some_list)//2]:
#
#         some_list = some_list[:len(some_list)//2+1]
#
#         print(some_list, len(some_list) // 2, some_list[len(some_list) // 2])
#         # print(element)
#         print('len_list:',len_list)
#
#     elif element > some_list[len(some_list)//2]:
#         # len_list += len(some_list)//2
#         len_list.append((len(some_list)//2)+1)
#         some_list = some_list[len(some_list)//2+1:]
#         # len_list += len(some_list) // 2
#         len_list.append((len(some_list) // 2)+1)
#         print(some_list, len(some_list) // 2, some_list[len(some_list) // 2])
#         # print(element)
#         print('len_list:',len_list)
#
#     # len_list += len(some_list)//2
#
# print('len_list:',len_list)
# print(some_list[len(some_list) // 2])
# print(sum(len_list)-1)




##solution

def solution(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    while start_index <= end_index :
        mid_point = (start_index + end_index) // 2


        if element == some_list[mid_point]:
            return mid_point

        elif element < some_list[mid_point]:
            end_index = mid_point-1
        else : start_index = mid_point+1

    return None

print(solution(element,some_list))