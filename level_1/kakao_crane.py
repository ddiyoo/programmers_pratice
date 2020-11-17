board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

### ddiyoo solution

line = []
answer = 0
for i in range(len(board)):
    test = []
    for j in range(len(board)):

        test.append(board[j][i])
    a = [a for a in test if a !=0]
    line.append(a)


# line = [[], [2, 5], [5, 4, 1], [4, 3], [2, 1]]
basket = []
for line_num in moves:

    if line[line_num-1] != []:
        basket.append(line[line_num - 1][0])
        del line[line_num - 1][0]
        # print(line)
        # print(line_num, basket)
        if len(basket) >=2:
            for k in range(len(basket) - 1):
                print(len(basket),basket)
                if basket[k] == basket[k+1]:
                    print(basket[k],basket[k+1])
                    del basket[k+1] ## k 부터 지운다면 뒤에 k+1이 k로 바뀜
                    del basket[k]
                    answer += 2

### other solution

def solution(board, moves):
    answer = 0
    linestack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                linestack.append(board[j][i-1])
                board[j][i-1] = 0
                if len(linestack) >= 2:
                    if linestack[-2] == linestack[-1]:
                        del linestack[-1]
                        del linestack[-1]
                        answer += 2
                break
    return answer



