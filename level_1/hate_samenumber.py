arr = [1,1,3,3,0,1,1]
# arr = [4,4,4,3,3]

### ddiyoo solution
### efficiency score 0....
def solution(arr):
    answer = []
    last_number = []
    for input in list(set(arr)):
        ## input의 위치값 담는 list
        input_index = []
        basket = arr
        while True:
            try:
                # print('basket:',basket, 'input_index:',input_index, 'basket_index:', basket.index(input))
                input_index.append(basket.index(input)+ (input_index[-1]+1 if len(input_index)!=0 else 0)) ## input의 첫 위치 + 두번째 위치
                basket = arr[input_index[-1]+1:]
            except:
                break
        if len(input_index) != 1:
            for i in range(len(input_index)-1):
                if input_index[i+1] - input_index[i] != 1:
                    last_number.append(input_index[i])
                if i == (len(input_index)-2):
                    last_number.append(input_index[len(input_index)-1])
        else : last_number.append(input_index[0])
    last_number = sorted(last_number)
    answer=list(map(lambda x : arr[x], last_number))
    return answer

print(solution(arr))









