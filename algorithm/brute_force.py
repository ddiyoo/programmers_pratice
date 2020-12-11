
# ##1
# def max_product(left_cards, right_cards):
#     answer = []
#     for i in range(len(left_cards)):
#         for j in range(len(right_cards)):
#             answer.append(left_cards[i]*right_cards[j])
#     return max(answer)
#     # 코드를 작성하세요.
#
#
# # 테스트
# print(max_product([1, 6, 5], [4, 2, 3]))
# print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
# print(max_product([-1, -7, 3], [-4, 3, 6]))
#


# ##2
# # 제곱근 사용을 위한 sqrt 함수
# from math import sqrt
#
#
# # 두 매장의 직선 거리를 계산해 주는 함수
# def distance(store1, store2):
#     return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)
#
#
# # 가장 가까운 두 매장을 찾아주는 함수
# def closest_pair(coordinates):
#     d_list = []
#     store_1 = []
#     store_2 = []
#     for i in range(0,len(test_coordinates)-1):
#         for j in range(i+1,len(test_coordinates)):
#             d_list.append(distance(test_coordinates[i],test_coordinates[j]))
#             store_1.append(test_coordinates[i])
#             store_2.append(test_coordinates[j])
#     d_index = d_list.index(min(d_list))
#     return [store_1[d_index], store_2[d_index]]
#
#
# # 여기 코드를 쓰세요
#
# # 테스트
# test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# print(closest_pair(test_coordinates))


###3
buildings[0]=3
buildings[1]=0
buildings[2]=4

basket =
def trapping_rain(buildings):
    if buildings[1] < buildings[0]:
        if buildings[1] < buildings[2]:
            if buildings[0] < buildings[2]:

                basket[1] += buildings[0] - buildings[1]
            else : basket += buildings[1] - buildings[0]
        else :

    




# 코드를 작성하세요

# 테스트
print(trapping_rain([3,0,4]))
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))