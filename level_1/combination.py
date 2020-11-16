from itertools import combinations
numbers = [2,1,3,4,1]

def solution(numbers):
    a = list(combinations(numbers, 2))
    answer = []
    for i in range(len(a)):    ### i in a 로 했으면 더 간단
        answer.append(a[i][0] + a[i][1])  ### i[0]+i[1]로 할 수 있음
    answer = list(set(answer))
    answer = sorted(answer)   ### answer.sort()

    return answer

print(solution(numbers))


#### 다른 정답

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
            print(i,j)
    return sorted(list(set(answer)))

print(solution(numbers))