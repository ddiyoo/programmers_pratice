s = "abcde"
s = "qwer"

def solution(s):
    answer = ''
    if len(s)%2 != 0:
        answer = s[(len(s)//2)]
    else :
        answer= s[(len(s)//2)-1:(len(s)//2)+1]
    return answer

print(5%2) ## result:1, 나머지
print(5//2) ## result:2, 몫


## other solution

def solution(s):

    return s[(len(s) - 1) // 2:len(s) // 2 + 1]
# s[(len(s)//2 -1):(len(s)//2 +1)]
print(solution(s))