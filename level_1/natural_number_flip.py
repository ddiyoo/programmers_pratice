n = 12345

def solution(n):
    answer=sorted((list(str(n))),)
    answer=list(map(int,answer))
    return answer

print(solution(n))

def solution2(n):
    n_list=str(n)
    if len(n_list) == 0 or len(n_list) ==1 :
        return n_list
    print(n_list)
    return n_list[-1:] + solution2(n_list[:-1])

def solution3(n):
    answer = []
    a=n
    while True:
        b = a % 10
        a = a // 10
        answer.append(b)
        if a<10:
            answer.append(a)
            break
    return answer

print(solution3(n))


