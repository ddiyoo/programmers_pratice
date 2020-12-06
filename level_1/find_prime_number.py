import time
start = time.time()

n = 100
basket = []

# for number in range(2,n):
#     if number%2 != 0:
#         basket.append(number)
# print(basket)


# number = list(range(2,n))
# list(map(lambda x: basket.append(x) if x%2 !=0 else False, number))
# print(basket)
# list(map(lambda x: basket.remove(x) if x%3 ==0 else False, basket))
# print(basket)



### 소수제곱 범위 구하기
prime_number_coverage = []
prime_number = [2,3,5,7]
for number in range(2,n):
    if number**2 <= n:
        prime_number_coverage.append(number)
print(prime_number_coverage)
list(map(lambda x: prime_number_coverage.remove(x) if x%2 ==0 else False, prime_number_coverage))
print(prime_number_coverage)


print(f"time:{time.time()-start}")

