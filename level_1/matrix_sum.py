arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

def solution(arr1, arr2):
    answer = []
    for i,j in list(zip(arr1, arr2)):
        basket= []
        for k,l in list(zip(i,j)):
            basket.append(k+l)
        answer.append(basket)
    return answer

print(solution(arr1,arr2))


