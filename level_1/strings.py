s = '1234567'

### ddiyoo solution
def solution(s):
    answer = True
    if len(s) == (4 or 6):
        try:
            int(s)
        except:
            answer = False
    else : answer =False
    return answer
print(solution(s))