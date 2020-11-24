element = 11
some_list = [2, 3, 5, 7, 11]

answer = None
for n, number in enumerate(some_list):
    while True:
        if element == number:
            answer = []
            answer = n+1
        break
print(answer)

