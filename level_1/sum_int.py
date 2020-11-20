a = 3
b = 3

###ddiyoo solution
def solution(a, b):
    answer = 0
    answer=sum(list(range(min(a,b),max(a,b)+1)))
    return answer

print(solution(a,b))


### other solution

def solution(a,b):

    if b > a : a, b = b, a

    return sum(list(range(a, b+1)))

print(solution(a,b))