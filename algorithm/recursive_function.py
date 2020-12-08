# def countdown(n):
#     if n>0:
#         print(n)
#         countdown(n-1)
#
# countdown(4)
#
# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n-1) * n
#
# print(factorial(4))

# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-2) + fib(n-1)
#
# for i in range(1, 11):
#     print(fib(i))

# # 1부터 n까지의 합을 리턴
# def triangle_number(n):
#     if n == 1:
#         return 1
#     return n+ triangle_number(n-1)
#     # 코드를 입력하세요
#
# # 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
# for i in range(1, 11):
#     print(triangle_number(i))

# n의 각 자릿수의 합을 리턴
# def sum_digits(n):
#     print(sum(list(map(int,list(str(n))))))
#     # 코드를 작성하세요.
#
# # 테스트
# print(sum_digits(22541))
# print(sum_digits(92130))
# print(sum_digits(12634))
# print(sum_digits(704))
# print(sum_digits(3755))

# def sum_digits(n):
#     if n < 10 :
#         return n
#     print(n % 10, sum_digits(n // 10))
#     return n % 10 + sum_digits(n // 10)
#
# print(sum_digits(22541))

# n= 22541
# print(n%10)  ## % 나머지
# print(n//10) ## / 몫
#
#
# # 파라미터 some_list를 거꾸로 뒤집는 함수
# def flip(some_list):
#     if len(some_list) == 0 or len(some_list) ==1 :
#         return some_list
#     return some_list[-1:] + flip(some_list[:-1])
#     # 코드를 입력하세요.
#
# # 테스트
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# some_list = flip(some_list)
# print(some_list)


def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))